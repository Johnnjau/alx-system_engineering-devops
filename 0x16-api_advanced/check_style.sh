#!/bin/bash

# Find all Python files in the current directory
files=$(find . -name "*.py")

# Run flake8 on each Python file
for file in $files; do
    flake8 --max-line-length=100 $file
done
