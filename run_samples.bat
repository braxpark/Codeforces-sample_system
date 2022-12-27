@echo off

set "idx=%1"
g++ "%idx%.cpp" -o "%idx%"

mkdir outputs 

"%1.exe" < "samples\%1.in" > "outputs\%idx%.outs"

check.exe "%1"
