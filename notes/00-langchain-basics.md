# LangChain Basics

## What is a Model in LangChain?
A model is a runnable that accepts messages and returns messages. `ChatOpenAI` is a chat model wrapper around OpenAI's API.

## Raw LLM Call vs Agent Call
- **Raw call**: Input → model → output. No tools, no state.
- **Agent call**: Input → model decides → calls tool(s) → model uses tool output → final output.