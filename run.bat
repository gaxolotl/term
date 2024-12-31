@echo off
REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b
)

REM Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed. Please install pip and try again.
    pause
    exit /b
)

REM Check if the "rich" library is installed
python -c "import rich" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing the "rich" library...
    pip install rich
    if %errorlevel% neq 0 (
        echo Failed to install the "rich" library. Please check your pip configuration.
        pause
        exit /b
    )
)

REM Start the application
python term-beta.py
