@echo off
title ETCHERO MULTITOOL V3 Launcher
color 0A
cls

echo ==================================================
echo      Starting ETCHERO MULTITOOL V3...
echo ==================================================
echo.

python ETCHERO.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ==================================================
    echo    ERROR: Something went wrong.
    echo    Ensure Python is installed and added to PATH.
    echo ==================================================
    echo.
    pause
)
