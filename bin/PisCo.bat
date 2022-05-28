@echo off
if not exist "%1" echo File Not Found & exit /b
for /f "usebackq tokens=*" %%i in (%1) do @PisCo_Kernel.exe %%i