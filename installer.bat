@ECHO OFF@ECHO OFF
:: Check for Python Installation
python --version 2>NUL
if errorlevel 1 goto errorNoPython

:: Check if virtualenv is installed
python check_venv.py
if NOT EXIST env\Scripts\activate (python -m venv env )
::Check if git is installed
git --version
if errorlevel 1 goto errorNoGit

:: Reaching here means Python and Virtualenviroment are installed
dir
CALL  env\Scripts\activate  
pip install -r requirements.txt

pushd %~dp0
cscript shortcutter.vbs

pause
goto:eof
:errorNoPython
echo.
echo Error^: Python not installed
:errorNoGit
echo.
echo Error^: Git not installed
pause
