@ECHO OFF
dir
CALL  %~dp0env\Scripts\activate  

python main.py
PAUSE
