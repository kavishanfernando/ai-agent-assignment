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
export GEMINI_API_KEY="your_api_key_here"
python main.py
```

## Testing Process

The project uses Python's built-in `unittest` framework. Tests are stored in the `tests/` directory and cover both the individual tools and the agent's test mode behavior.

Run all tests with:

```bash
python3 -m unittest discover -s tests
```

## Test Scenarios

- Calculator valid expression: checks that a simple arithmetic expression returns the expected result.
- Calculator invalid expression: checks that invalid input returns an error message instead of crashing.
- File reader missing file: checks that a missing file path returns a readable error message.
- Translation tool: checks that the translation tool returns a string response.
- Time tool: checks that the time tool returns the current local date and time as text.
- Agent calculator request: checks that the agent can handle a calculator-style request in test mode.
- Agent file reader request: checks that the agent can handle a file-reading request in test mode.
- Agent translation request: checks that the agent can handle a translation request in test mode.
- Agent unknown input: checks that unsupported input returns a clear fallback response.

## Deployment Preparation

The system can be run as a local command-line application. A Python virtual environment should be created, dependencies should be installed from `requirements.txt`, and the `GEMINI_API_KEY` environment variable should be set before starting `main.py`.

## Data Conversion / Porting

No external data conversion or porting is required. The system receives user input as plain text, passes structured arguments to tools when needed, and returns tool results as strings.
