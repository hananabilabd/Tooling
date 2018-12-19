@echo off                              
set /p text=Please Enter Text:
set /p folder=Please Enter Folder Name:
set /p file=Please Enter File Name:
if not exist %folder% (
mkdir %folder%
)
echo %text% >%folder%\%file%.txt
set /p v= Press any key to exit ... 
  