#!/bin/bash
index=$1
g++ $index.cpp -o $index


[[ -d outputs ]] || mkdir outputs

./$index < samples/$index.in > outputs/$index.outs

./check $index
