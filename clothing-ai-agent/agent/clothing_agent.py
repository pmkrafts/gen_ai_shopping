import json
import logging
import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage, ToolMessage

from tools import (
    search_products_tool,
    get_product_details_tool,
    get_recommendations_tool,
    manage_cart_tool,
    size_fit_advisor_tool,
    budget_occasion_planner_tool,
    get_trending_styles_tool,
    analyze_image_tool,
    image_search_tool,
    manage_wishlist_tool,
    process_order_tool,
)
from agent.styling_session_store import create_session, update_session, get_session
from models.response import AgentResponse

load_dotenv()

SYSTEM_PROMPT = """You are a helpful AI shopping assistant for a clothing store.
You can search products, show details, give recommendations, manage the cart and wishlist,
advise on size & fit, plan outfits by budget and occasion, suggest trending styles,
analyze clothing images, search by image, process orders, and run multi-turn styling sessions.
Always respond with a friendly, concise reply and suggest one or two next actions.
"""

# Module-level agent instance so it is built only once.
_agent = None

# In-memory conversation store: session_id -> list of BaseMessage objects.
_memory_store: dict[str, list[BaseMessage]] = {}

# Logging setup
_LOG_DIR = Path(__file__).parent.parent / "logs"
_LOG_DIR.mkdir(exist_ok=True)
_log_file = _LOG_DIR / f"agent_{datetime.now().strftime('%Y%m%d')}.log"

logging.basicConfig(
    filename=_log_file,
    level=logging.INFO,
    format="%(asctime)s %(message)s",
)


def _log_event(event_type: str, data: dict) -> None:
    """Append a structured JSON line to the agent log."""
    try:
        logging.info(json.dumps({"event": event_type, **data}, default=str))
    except Exception:
        pass


def _extract_tool_calls(messages: list[BaseMessage]) -> list[dict]:
    """Extract tool calls and tool results from the agent message stream."""
    tool_calls = []
    for msg in messages:
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            for tc in msg.tool_calls:
                tool_calls.append({
                    "type": "tool_call",
                    "name": getattr(tc, "name", None),
                    "args": getattr(tc, "args", None),
                })
        elif isinstance(msg, ToolMessage):
            tool_calls.append({
                "type": "tool_result",
                "tool_call_id": getattr(msg, "tool_call_id", None),
                "content": getattr(msg, "content", None)[:200],
            })
    return tool_calls


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
            analyze_image_tool,
            image_search_tool,
            manage_wishlist_tool,
            process_order_tool,
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


def _detect_styling_intent(text: str) -> bool:
    """Detect if the user wants to start or continue a styling session."""
    keywords = [
        "styling session",
        "beach vacation",
        "vacation outfit",
        "wedding outfit",
        "party outfit",
        "plan outfits",
        "help me choose",
    ]
    return any(keyword in text.lower() for keyword in keywords)


def _build_styling_context() -> str:
    """Return a text summary of the active styling session, if any."""
    session = get_session()
    if session is None:
        return ""
    return (
        f"\n\nActive styling session:\n"
        f"- Goal: {session.goal}\n"
        f"- Budget: {session.budget}\n"
        f"- Selected items: {len(session.selected_items)}\n"
        f"- Feedback so far: {session.feedback}\n"
        f"- Turn: {session.turn_count}"
    )


def run_agent(
    input_text: str,
    chat_history: list | None = None,
    session_id: str = "default",
) -> dict:
    """Run the agent with conversation memory, styling sessions, and logging.

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

    # Manage styling session state.
    if _detect_styling_intent(input_text):
        session = get_session()
        if session is None:
            create_session(goal=input_text)
        update_session(turn_count=(get_session().turn_count + 1 if get_session() else 1))

    # Build message list from memory + styling context + current input.
    messages = list(memory)
    styling_context = _build_styling_context()
    if styling_context:
        messages.append(
            HumanMessage(content=f"[System context for assistant]{styling_context}")
        )
    messages.append(HumanMessage(content=input_text))

    try:
        raw = agent.invoke({"messages": messages})
        output = raw["messages"][-1].content
        error = None
    except Exception as e:
        output = "I'm sorry, something went wrong. Please try again."
        error = str(e)

    # Persist this turn in memory.
    memory.append(HumanMessage(content=input_text))
    memory.append(AIMessage(content=output))

    # Log the interaction.
    _log_event(
        "agent_run",
        {
            "session_id": session_id,
            "input": input_text,
            "tool_calls": _extract_tool_calls(raw.get("messages", [])) if "raw" in locals() else [],
            "output": output,
            "error": error,
        },
    )

    # Try to parse into AgentResponse; fall back to wrapping raw text.
    try:
        return AgentResponse(reply=output, products=[]).model_dump()
    except Exception:
        return {"reply": str(output), "products": [], "cart": None, "suggested_actions": []}


def clear_memory(session_id: str = "default") -> None:
    """Clear conversation memory for a session."""
    if session_id in _memory_store:
        _memory_store[session_id].clear()


def clear_styling_session() -> None:
    """Clear the active styling session."""
    from agent.styling_session_store import clear_session
    clear_session()
