@ECHO OFF
SETLOCAL EnableDelayedExpansion
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do     rem"') do (
  set "DEL=%%a"
)

goto start

:noPython
echo Error^: Python not installed... visit www.python.org/downloads/ to download Python
echo Error^: Exiting in 30 seconds...
PING localhost -n 36 >NUL
echo Exiting...
exit

:pipInstalls
pip install overwatch-api
pip install discord

if errorlevel 0 call :colorEcho a0 "Success, exiting in 30 seconds"
PING localhost -n 36 >NUL
exit

:emptyInput

call :colorEcho c0 "No token entered, please retry or exit this window.."
echo .
echo [RESTART]
goto start

:start

set /p botToken="Enter Discord bot Token: "

if "%botToken%" equ "" goto emptyInput

echo %botToken% >> ./token.txt

:: Now let's check if Python is installed
python --version 2>NUL
if errorlevel 1 goto noPython
if errorlevel 0 goto pipInstalls

::To color text
:colorEcho
echo off
<nul set /p ".=%DEL%" > "%~2"
findstr /v /a:%1 /R "^$" "%~2" nul
del "%~2" > nul 2>&1i

