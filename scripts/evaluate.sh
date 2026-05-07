#!/bin/bash

# This script evaluates the performance of the AI agent system.

# Set the environment variables
export PYTHONPATH=$(pwd)/src

# Run the evaluation script
python3 -m src.pipelines.orchestration --evaluate

# Capture the exit status
if [ $? -eq 0 ]; then
    echo "Evaluation completed successfully."
else
    echo "Evaluation failed."
    exit 1
fi

# Optionally, you can add commands to log the results or send notifications here.