"""
LangGraph + MCP Demo - ZERO Credit Cards Needed!
Shows GitHub + Filesystem capabilities
Perfect for client demos
"""

import asyncio
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0,api_key = os.getenv("OPENAI_API_KEY"))

async def main():
    
    mcp_config = {}
    
    # Test Filesystem
    try:
        test_config = {
            "filesystem": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-filesystem", os.path.abspath(".")],
                "transport": "stdio"
            }
        }
        client = MultiServerMCPClient(test_config)
        tools = await client.get_tools()
        tools_list = [tool.name for tool in tools]
        print(f"test_tools: {tools_list}")

        mcp_config["filesystem"] = test_config["filesystem"]

        print(f"   ✅ Filesystem server working\n {mcp_config}")

    except Exception as e:
        print(f"   ❌ Filesystem server failed: {e}\n")

    return tools

async def run_agent():
    tools = await main()
    agent = create_agent(llm, tools)

    while True:
        # Note: input() is blocking; in production async apps, 
        # you'd use an async input method, but this works for scripts.
        user_input = input("Enter your question (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        
        # Await the async call
        response = await agent.ainvoke({'messages':[{'role':'user','content':user_input}]})
        
        # Extract the text from the message list
        print(f"Agent Response: {response['messages'][-1].content}\n")

if __name__ == "__main__":
    asyncio.run(run_agent())