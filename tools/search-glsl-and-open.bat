@echo off
setlocal enabledelayedexpansion

if exist src\ (
	rd /s /q .\src\
	echo Cleaning temp folder \src
	)
if exist *.material.bin (
	del .\*.material.bin
	echo Cleaning temp file material.bin
	)
echo.

::========================================
::	set MBT=MaterialBinTool-0.8.2-all.jar
::	set MBT=MaterialBinTool-0.9.0-all.jar
	set MBT=MaterialBinTool-0.9.1-all.jar
::========================================

set n=0
set input=folders
::set /p input=Drag or Input a folder here:  
echo Continue process glsl?
pause

:: for /r .\ %%g in (*.glsl) do (start %%g)

for /r %input% %%i in (*.material.bin) do (
	set /a n+=1
	echo.
	copy /y %%i %%~nxi >nul
	echo Opening !n!th file...
	java -jar .\%MBT% -u .\%%~nxi -o .\src\
	if not exist src\ (
		set /a n-=1
		echo Error.
		del %%~nxi
		goto end
	)
	python glsl_reduce.py
	java -jar .\%MBT% -r .\src\* -o .\ 
	echo OK.
	copy /y %%~nxi %%i >nul
	del %%~nxi
	rd /s /q .\src\
)

:end
echo.
echo.
echo Success. %n% files in total
echo.
timeout -t 2 >nul
pause




