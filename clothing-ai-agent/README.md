# Clothing Store AI Agent

A learning-focused AI agent for a clothing store built with **Python**, **LangChain**, **OpenAI**, and **Pydantic v2**.

The agent understands natural language, calls tools, manages cart/wishlist state, gives personalized recommendations, handles mock checkout, and supports multi-turn styling sessions — all through a simple CLI.

---

## Features

- Natural language product search
- Product details and comparison
- Personalized outfit recommendations
- "Complete the look" suggestions
- Cart and wishlist management via chat
- Size and fit advice
- Budget and occasion outfit planning
- Trending style suggestions
- Mock checkout and order processing
- Image-based visual search (mock)
- Multi-turn styling sessions with memory
- Guardrails, retry logic, and structured logging

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.11+ |
| Agent Framework | LangChain / LangGraph |
| LLM | OpenAI GPT-4o-mini |
| Structured Outputs | Pydantic v2 |
| Persistence | In-memory |
| Interface | CLI |
| Testing | pytest |
| Linting/Formatting | ruff |

---

## Project Structure

```text
clothing-ai-agent/
├── agent/              # Agent logic, prompts, guardrails, memory
├── tools/              # LangChain tool functions
├── models/             # Pydantic v2 schemas
├── data/               # Seed product catalog + store module
├── tests/              # Unit, tool, use-case, and conversation tests
├── logs/               # Structured agent logs
├── main.py             # CLI entry point
├── requirements.txt
├── .env
└── README.md
```

---

## Setup

1. Clone or navigate to the project:

   ```bash
   cd clothing-ai-agent
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # Windows
   .\.venv\Scripts\Activate.ps1
   # macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create your environment file:

   ```bash
   cp .env.example .env
   ```

5. Add your OpenAI API key to `.env`:

   ```text
   OPENAI_API_KEY=sk-...
   ```

---

## Run the CLI

```bash
python main.py
```

Run with debug output:

```bash
python main.py --debug
```

---

## Demo Prompts

Try these in the CLI:

```text
Show me red dresses under 1500 INR in size M
Tell me about PROD001
Recommend a casual outfit for a 25-year-old woman
Add PROD001 to my cart
Show my cart
I'm 5'10", 75kg, broad shoulders. What size shirt?
Plan a wedding guest outfit under 5000 INR
What are the trending styles this monsoon in India?
Save PROD002 to my wishlist
Checkout, I'm Aarav Sharma in Mumbai
I need clothes for a beach vacation
```

---

## Running Tests

```bash
python -m pytest
```

Run with verbose output:

```bash
python -m pytest -v
```

Run a specific test file:

```bash
python -m pytest tests/use_cases/test_uc01_search.py -v
```

---

## Makefile Commands

```bash
make test      # Run all tests
make run       # Run the CLI
make debug     # Run the CLI in debug mode
make lint      # Run ruff linter
make format    # Run ruff formatter
```

---

## Linting and Formatting

```bash
ruff check .
ruff format .
```

---

## Logs

Agent interactions are logged to:

```text
logs/agent_YYYYMMDD.log
```

Each line is a JSON object containing the input, tool calls, output, and any errors.

---

## Success Definition

The project is complete when a user can run `python main.py`, hold a multi-turn conversation about clothing, search products, manage a cart, checkout, and every agent reply is validated by Pydantic.
