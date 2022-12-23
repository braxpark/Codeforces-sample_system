#!/bin/bash

contest=$1

currDir=$(pwd)
echo $contest
echo $currDir
python3 getProblems.py $currDir/$contest $contest
g++ checkProblems.cpp -o check
cp check $currDir/$contest
cp run_samples.sh $currDir/$contest
cd $currDir/$contest
chmod +x ./run_samples.sh

