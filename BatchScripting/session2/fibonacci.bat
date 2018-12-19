@echo off
setlocal EnableDelayedExpansion
set first=0 
set second=1 
set next=0
set counter=0
set /p n= Enter Number of terms:

IF  %n% LEQ -1 (
 ECHO No Negative Numbers is allowed Please Enter postive
 exit /b
)
set /a end=!n!-1
for /l %%a IN (0,1,!end!) do (
  set /a counter=%%a
IF  !counter! LEQ 1 (
     set /a next=!counter!
) ELSE (
	 set /a next =!first!+!second!
     set /a first=!second!
     set /a second=!next!
)
	  
echo !next! 

)
