@echo off
cd /d %~dp0

echo Checking Streamlit...
pip show streamlit >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Installing Streamlit...
    pip install streamlit pandas
)

echo Starting App...
streamlit run app.py

pause
