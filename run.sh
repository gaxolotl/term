#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Please install Python and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip is not installed. Please install pip and try again."
    exit 1
fi

# Check if the "rich" library is installed
python3 -c "import rich" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing the 'rich' library..."
    pip3 install rich
    if [ $? -ne 0 ]; then
        echo "Failed to install the 'rich' library. Please check your pip configuration."
        exit 1
    fi
fi

# Start the application
python3 term-beta.py
