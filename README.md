# AI Agent Assignment

This project implements a modular command-line interface personal assistant in Python that utilizes Google Gemini API․

## Features

- Natural language CLI assistant
- Session-based conversation memory
- Dynamic tool usage through Gemini function calling
- ReAct-style reasoning flow
- Robust error handling

## Tools

1. CalculatorTool
2. TimeTool
3. TranslationTool
4. FileReaderTool

## Architecture

- Agent
- MemoryManager
- ToolRegistry
- BaseTool
- tools/

## Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export GEMINI_API_KEY="your_api_key"
python main.py