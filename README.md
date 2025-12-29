# Minimal_mcp_filesystem_program
This code demonstrates how to bridge the Model Context Protocol (MCP) with LangGraph to give an AI agent direct access to local system resources. It sets up a filesystem server via npx, enabling the LLM to read, write, and manage local files securely using standard MCP adapters.
LangGraph + MCP Filesystem Demo
This project provides a "Zero Credit Card" proof-of-concept for integrating the Model Context Protocol (MCP) with LangGraph. It allows a GPT-4o-mini agent to interact directly with your local filesystem (read/write/list files) using a standardized server-client architecture.

🚀 Key Features
Local Tooling: Uses @modelcontextprotocol/server-filesystem to expose local directories as tools.

Agentic Workflow: Utilizes LangGraph/LangChain to handle tool calling and reasoning.

No Overhead: Demonstrates how to connect external data sources to LLMs without complex custom API integrations.

📋 Prerequisites
Node.js & npm: (Required for npx to run the MCP server).

Python 3.10+

OpenAI API Key: For the gpt-4o-mini model.

🛠️ Setup
Clone the repository (or save the script as main.py).

Install Python dependencies:

Bash

pip install langchain-openai langchain-mcp-adapters python-dotenv
Configure Environment: Create a .env file in the root directory:

Code snippet

OPENAI_API_KEY=your_key_here
🏃 How to Run
Execute the script using:

Bash

python main.py
The script will initialize a local filesystem server scoped to the current directory.

Once the "✅ Filesystem server working" message appears, you can talk to the agent.

Try asking:

"What files are in the current directory?"

"Create a file named notes.txt and write 'Hello MCP' inside it."

"Read the contents of the .env file (but don't show my key)."

🔍 How it Works
The script uses the MultiServerMCPClient to connect to a standard MCP server via stdio.

Server: npx -y @modelcontextprotocol/server-filesystem

Client: The LangChain MCP Adapter converts these MCP tools into a format the LLM can understand.

Execution: The agent decides which filesystem tool to call based on your prompt, executes it locally, and reports the result.
