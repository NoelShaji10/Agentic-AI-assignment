import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from duckduckgo_search import DDGS

@tool
def search_tool(query: str) -> str:
    """Search the web for the given query."""
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=3)]
            return str(results)
    except Exception as e:
        return f"Search failed: {e}"

# Load environment variables
load_dotenv()

def create_research_agent():
    # Initialize the Groq LLM
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.2,
    )

    # Initialize the tools
    # (search_tool is defined globally with @tool)
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

    tools = [
        search_tool,
        wikipedia
    ]

    # Initialize the agent using LangGraph
    agent = create_react_agent(llm, tools)

    return agent

def run_research(topic: str):
    agent = create_research_agent()
    
    prompt = f"""
You are an autonomous research agent. Your task is to research the following topic: "{topic}".

DO NOT get stuck in an infinite loop! Do a maximum of 2 tool calls.
Once you have gathered any information, stop querying and synthesize it into a detailed, well-structured report.

The report should include:
1. An introduction to the topic
2. Key insights and detailed findings
3. A conclusion

Format the final output cleanly in Markdown.
"""


    print(f"Starting research on topic: '{topic}'...\n")
    try:
        config = {"recursion_limit": 5}
        response = agent.invoke({"messages": [("user", prompt)]}, config=config)
        final_message = response["messages"][-1].content
        
        # Save report to a file
        filename = topic.replace(" ", "_").replace("/", "_").lower() + "_report.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(final_message)
            
        print(f"\nResearch complete! Report saved to {filename}")
        return final_message
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Autonomous Research Agent using LangChain and Groq")
    parser.add_argument("topic", type=str, nargs="?", default="Impact of AI in Healthcare", help="The topic to research")
    args = parser.parse_args()
    
    report = run_research(args.topic)
    
    if report:
        print("\n\n=== FINAL REPORT ===\n")
        print(report)
