@echo off 
for /f "tokens=1-3" %%G in (
"helloworld" "outputFolder" "output.txt"
) DO (
createFolderFileTxt.bat %%G %%H %%I
)