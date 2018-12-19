@echo off
set folder_name=%1
set file_name=%2
set text=%3
set result=false
if [%1] == [] set result=true
if [%2] == [] set result=true
if [%3] == [] set result=true
if "%result%" == "true" (
    echo Invalid Input Please Enter valid 3 argument
	exit /b
)
if not exist %folder_name% (
mkdir %folder_name%
)
echo %text% >%folder_name%\%file_name%.txt
set /p v= Press any key to exit ... 