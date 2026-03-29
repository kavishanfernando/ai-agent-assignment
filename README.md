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
pip install -r requirements.txthttps://docs.github.com/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
export GEMINI_API_KEY="AIzaSyAscIdld6hMm7N8WxQtQXE1YJaWHRDWpFo"
python main.py
