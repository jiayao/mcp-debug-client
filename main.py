import asyncio
import argparse
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient
from mcp_use.logging import Logger

async def main():
    parser = argparse.ArgumentParser(description='Run MCP agent with custom config')
    parser.add_argument('--config', '-c', default="mcp.json")
    parser.add_argument('--log_level', '-l', type=int, default=1, 
                        help='Log level: 1 for INFO, 2 for DEBUG')
    args = parser.parse_args()
    Logger.set_debug(args.log_level)
    client = MCPClient.from_config_file(args.config)
    llm = ChatOpenAI(model="gpt-4o-mini")
    agent = MCPAgent(llm=llm, client=client, max_steps=30)
    await agent.run(
        "what's on https://github.com/trending?",
    )

if __name__ == "__main__":
    asyncio.run(main())