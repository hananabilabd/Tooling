@echo off
setlocal EnableDelayedExpansion
set fact=1
set /p n= To calculate factorial , Enter Number:
IF %n%==0 (
    ECHO Factorial of 0=1
	exit /b
)
IF  %n% LEQ -1 (
 ECHO No Factoral to negative
 exit /b
)
for /l %%a IN (1,1,!n!) do (
rem echo %%a
set /a fact=%%a * !fact!

)
rem there is no differnce if i did $ echo Factorial=%fact%  or $ echo Factorial=%fact% in the last line 
echo Factorial=%fact%