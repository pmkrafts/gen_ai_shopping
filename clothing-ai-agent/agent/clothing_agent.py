import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage

from tools import (
    search_products_tool,
    get_product_details_tool,
    get_recommendations_tool,
    manage_cart_tool,
    size_fit_advisor_tool,
    budget_occasion_planner_tool,
    get_trending_styles_tool,
)
from models.response import AgentResponse

load_dotenv()

SYSTEM_PROMPT = """You are a helpful AI shopping assistant for a clothing store.
You can search products, show details, give recommendations, manage the cart,
advise on size & fit, plan outfits by budget and occasion, and suggest trending styles.
Always respond with a friendly, concise reply and suggest one or two next actions.
"""

# Module-level agent instance so it is built only once.
_agent = None

# In-memory conversation store: session_id -> list of BaseMessage objects.
_memory_store: dict[str, list[BaseMessage]] = {}


def _get_agent():
    global _agent
    if _agent is None:
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
        tools = [
            search_products_tool,
            get_product_details_tool,
            get_recommendations_tool,
            manage_cart_tool,
            size_fit_advisor_tool,
            budget_occasion_planner_tool,
            get_trending_styles_tool,
        ]
        _agent = create_react_agent(llm, tools, prompt=SYSTEM_PROMPT)
    return _agent


def get_memory(session_id: str = "default") -> list[BaseMessage]:
    """Get or create conversation memory for a session."""
    if session_id not in _memory_store:
        _memory_store[session_id] = []
    return _memory_store[session_id]


def _convert_chat_history(chat_history: list) -> list[BaseMessage]:
    """Convert dict or BaseMessage chat history into LangChain message objects."""
    messages = []
    for msg in chat_history:
        if isinstance(msg, BaseMessage):
            messages.append(msg)
        elif isinstance(msg, dict):
            role = msg.get("role")
            content = msg.get("content", "")
            if role == "user":
                messages.append(HumanMessage(content=content))
            elif role == "assistant":
                messages.append(AIMessage(content=content))
    return messages


def run_agent(
    input_text: str,
    chat_history: list | None = None,
    session_id: str = "default",
) -> dict:
    """Run the agent with conversation memory.

    Args:
        input_text: The current user message.
        chat_history: Optional list of previous messages. Used if no session memory exists.
        session_id: Identifier for the conversation session.
    """
    agent = _get_agent()
    memory = get_memory(session_id)

    # Seed memory from explicit chat_history on first call if provided.
    if chat_history and not memory:
        memory.extend(_convert_chat_history(chat_history))

    # Build message list from memory + current input.
    messages = list(memory)
    messages.append(HumanMessage(content=input_text))

    raw = agent.invoke({"messages": messages})
    output = raw["messages"][-1].content

    # Persist this turn in memory.
    memory.append(HumanMessage(content=input_text))
    memory.append(AIMessage(content=output))

    # Try to parse into AgentResponse; fall back to wrapping raw text.
    try:
        return AgentResponse(reply=output, products=[]).model_dump()
    except Exception:
        return {"reply": str(output), "products": [], "cart": None, "suggested_actions": []}


def clear_memory(session_id: str = "default") -> None:
    """Clear conversation memory for a session."""
    if session_id in _memory_store:
        _memory_store[session_id].clear()
