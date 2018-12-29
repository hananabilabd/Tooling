@echo off  
setlocal EnableDelayedExpansion                            
for  /f "tokens=1-4" %%a in (input.txt) DO (
	if not exist %%a (
	mkdir %%a
	)
	if not exist %%b ( echo 0 > %%b ) else ( 
		for  /f "tokens=1" %%f in (%%b) DO (
			set /a x=%%f+1
			echo !x! > %%b
		 )
	)
	if not exist %%c ( echo 0 > %%c ) else ( 
		for  /f "tokens=1" %%g in (%%c) DO (
			set /a y=%%g+1
			echo !y! > %%c
		 )
	)
	if not exist %%d ( echo 0 > %%d ) else ( 
		for  /f "tokens=1" %%h in (%%d) DO (
			set /a z=%%h+1
			echo !z! > %%d
		 )
	)

)
if not exist "Text Files" (
mkdir "Text Files"
)
copy *.txt "Text Files"
if not exist "Sources Files" (
mkdir "Sources Files"
)
copy *.c "Sources Files"
if not exist "Header Files" (
mkdir "Header Files"
)
copy *.h "Header Files"