@echo off                              
set /p x= Please Enter x:
set /p o=Please Enter operation:
set /p y= Please Enter y:
set /A z=x%o%y
echo Result of  %x% %o% %y% = %z%
set /p v= Press any key to exit ... 
  