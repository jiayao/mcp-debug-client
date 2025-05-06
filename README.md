## Usage

First install [uv](https://docs.astral.sh/uv/getting-started/installation/)

```
uv sync

python main.py
```

## Example output

```
2025-05-05 21:41:46,358 - mcp_use - INFO - 🚀 Initializing MCP agent and connecting to services...
2025-05-05 21:41:46,358 - mcp_use - INFO - 🔌 Found 0 existing sessions
2025-05-05 21:41:46,358 - mcp_use - INFO - 🔄 No active sessions found, creating new ones...
2025-05-05 21:41:48,525 - mcp_use - INFO - ✅ Created 1 new sessions
2025-05-05 21:41:48,528 - mcp_use - INFO - 🛠️ Created 1 LangChain tools from client
2025-05-05 21:41:48,528 - mcp_use - INFO - 🧰 Found 1 tools across all connectors
2025-05-05 21:41:48,528 - mcp_use - INFO - 🧠 Agent ready with tools: fetch
2025-05-05 21:41:48,531 - mcp_use - INFO - ✨ Agent initialization complete
2025-05-05 21:41:48,531 - mcp_use - INFO - 💬 Received query: 'what's on https://github.com/trending?'
2025-05-05 21:41:48,531 - mcp_use - INFO - 🏁 Starting agent execution with max_steps=30
2025-05-05 21:41:48,531 - mcp_use - INFO - 👣 Step 1/30
2025-05-05 21:41:54,174 - mcp_use - INFO - 🔧 Tool call: fetch with input: {'url': 'https://github.com/trending'}
2025-05-05 21:41:54,174 - mcp_use - INFO - 📄 Tool result: Contents of https://github.com/trending: ## [hacksider / Deep-Live-Cam](/hacksider/Deep-Live-Cam)...
2025-05-05 21:41:54,174 - mcp_use - INFO - 👣 Step 2/30
2025-05-05 21:42:05,313 - mcp_use - INFO - ✅ Agent finished at step 2
2025-05-05 21:42:05,313 - mcp_use - INFO - 🎉 Agent execution complete
```