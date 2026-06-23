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
)
from models.response import AgentResponse

load_dotenv()

SYSTEM_PROMPT = """You are a helpful AI shopping assistant for a clothing store.
You can search products, show details, give recommendations, and manage the cart.
Always respond with a friendly, concise reply and suggest one or two next actions.
"""


def build_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    tools = [
        search_products_tool,
        get_product_details_tool,
        get_recommendations_tool,
        manage_cart_tool,
    ]

    agent = create_react_agent(llm, tools, prompt=SYSTEM_PROMPT)
    return agent


def run_agent(input_text: str, chat_history: list | None = None) -> dict:
    agent = build_agent()

    messages = []
    if chat_history:
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
    messages.append(HumanMessage(content=input_text))

    raw = agent.invoke({"messages": messages})
    output = raw["messages"][-1].content

    # Try to parse into AgentResponse; fall back to wrapping raw text
    try:
        return AgentResponse(reply=output, products=[]).model_dump()
    except Exception:
        return {"reply": str(output), "products": [], "cart": None, "suggested_actions": []}
