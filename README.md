# Codeforces-sample_system

This is my personal system for CLI sample/test cases for codeforces. It involves scraping for information related to contests -- problem count, problem indexes, and then subsequent test case input/output for each index. This assumes the use of c++. The check problem system checks the output via standard output from each indexed cpp file and compares to the file contents designated by {index}.out, previously scraped from codeforces.

## Usage

To use, simply clone the repo. Then run the gen_problems script with a contest number as a param. For example

`bash gen_problems.sh 1772`

This will generate that propblem files corresponding to the indexes from the given contest. Then, it generates the test case in and out files needed to run the check command. To test, here is an example: `./run_samples.sh A`. This runs the samples for problem A against the source file A.cpp.

## Customization

Assuming the use of cpp, just change the Template.cpp. This will subsequently change the generated source files for each index of the contest.
