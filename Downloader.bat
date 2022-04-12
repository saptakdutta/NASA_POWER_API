@echo off
call activate POWER

@echo on
python worker.py

@echo off
call conda deactivate
pause
goto :eof