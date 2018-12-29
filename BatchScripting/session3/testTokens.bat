@echo off 
rem for loop but in one iteration
for /f "tokens=1-3" %%a in ("helloworld outputFolder output.txt"
) DO (
echo %%a %%b %%c %%d
)
rem the same above for loop but not one iteration
rem we can use space , comma , dot as a delimetter
for  %%a in (helloworld outputFolder output.txt) DO (
echo %%a
)
for  /f "tokens=1-3" %%a in (input.txt) DO (
echo %%a %%b %%c
 )