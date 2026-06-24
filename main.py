import argparse
from agent.clothing_agent import run_agent


def main():
    parser = argparse.ArgumentParser(description="Clothing Store AI Agent")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Print reasoning details for each turn.",
    )
    args = parser.parse_args()

    print("🛍️  Clothing AI Agent")
    print("Type 'exit' or 'quit' to leave.\n")

    chat_history = []
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        response = run_agent(user_input, chat_history)

        if args.debug:
            print(f"[DEBUG] Response object: {response}")

        print(f"Agent: {response['reply']}\n")

        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": response["reply"]})


if __name__ == "__main__":
    main()
