@echo off 
rem let user enter x value                                
set /p x= Please Enter x:
rem arithematic operation
set /A x=x+1 
rem use %x% to substitute   
echo %x%   