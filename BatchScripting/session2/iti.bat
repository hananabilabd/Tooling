@echo off
rem echo %~a1
setlocal EnableDelayedExpansion
set x=0
for /l %%a IN (0,1,6) do (
rem echo %%a
set /a x=!x!+%%a
echo !x!
)
set /a y =x
echo %y%