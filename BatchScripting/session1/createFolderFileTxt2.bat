@echo off                              
set /p text=Please Enter Text:
set /p folder=Please Enter Folder Name:
set /p file=Please Enter File Name:
if exist %folder% (
goto Afterfolder
)
mkdir %folder%
:Afterfolder
cd %folder%
echo %text% > %file%.txt
cd ..
set /p v= Press any key to exit ... 
  