# adk-playwright-mcp

A Python agent for web automation using Google ADK and Playwright MCP.

## Overview

This project does web automation agent powered by [google-adk](https://github.com/google/adk-python) and [@playwright/mcp](https://github.com/microsoft/playwright-mcp). The agent can:

- Navigate to web pages
- Take screenshots
- Fill forms
- Click elements
- Search the web using browser tools

## Installation

1. **Python dependencies**
   Ensure you have Python 3.12+ installed and [uv installed](https://docs.astral.sh/uv/getting-started/installation/)

   ```zsh
   uv sync && source .venv/bin/activate
   ```
2. Install npx, it comes with node.js

## Usage

Run the dev web ui using `adk web` and the dev UI should show up in `http://localhost:8000`

## Configuration

- Be sure to configure the model of your choice
- I'm using Gemini, so we need to set `GEMINI_API_KEY` in the .env file in the project root.

## Credits

- [google-adk](https://github.com/google/adk-python)
- [@playwright/mcp](https://github.com/microsoft/playwright-mcp)
