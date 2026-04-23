# main.py
from agent import create_react_agent


def detect_tool_usage(messages):
    for msg in messages:
        if msg.type == "tool":
            if "get_weather" in msg.name:
                return "Calls Weather Tool → gets data"
            if "web_search" in msg.name:
                return "Calls Web Search Tool → summarizes data"
    return ""


def main():
    agent = create_react_agent()

    print("\n🤖 AI Research Agent")
    print("Type 'exit' to quit\n")

    while True:
        query = input("User: ").strip()
        if query.lower() == "exit":
            print("👋 Goodbye!")
            break

        result = agent.invoke({
            "messages": [{"role": "user", "content": query}]
        })

        messages = result["messages"]

        # Get final assistant answer
        answer = ""
        for msg in reversed(messages):
            if msg.type == "ai" and msg.content:
                answer = msg.content
                break

        # Detect tool usage
        tool_trace = detect_tool_usage(messages)

        # Output
        print("\n🤖:", end=" ")
        if tool_trace != "":
            print(f"{tool_trace}\n      {answer}")
        else:
            print(f"{answer}")

        print("-" * 60)


if __name__ == "__main__":
    main()
