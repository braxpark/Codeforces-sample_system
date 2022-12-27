@echo off
set "contest=%1"
set "currDir=%CD%"
set "contestDir=%CD%\%contest%"
echo %contestDir%
echo %contest%

python3 getProblems.py %contestDir% %contest%
g++ checkProblems.cpp -o check

copy check.exe %contestDir%
copy run_samples.bat %contestDir%

pushd %contestDir%
:: call run_samples.bat





