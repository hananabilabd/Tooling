@echo off
setlocal EnableDelayedExpansion
for  /f "tokens=1" %%a in (text1.txt) DO (
set /a x=%%a+1
echo !x! > text1.txt
 )