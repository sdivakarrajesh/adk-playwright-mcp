from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams, StdioServerParameters


root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name='playwright_automator_agent',
    instruction=(
        "You are an expert web automation agent. "
        "You can navigate to web pages, take screenshots, fill forms, and click elements. "
        "When asked to interact with a web page, use the appropriate browser tools. "
        "Always confirm successful navigation before attempting other actions on a page."
        "If you don't know something, you can always google it using the browser tools"
    ),
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command='npx',
                args=[
                    "-y",
                    "@playwright/mcp@latest",
                ],
                ),
                timeout=30
            ),
            # tool_filter=['browser_navigate', 'browser_screenshot', 'browser_fill', 'browser_click']
        )
    ],
)