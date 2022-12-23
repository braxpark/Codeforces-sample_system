#!/usr/bin/env python3

import os
from sys import argv
import requests
from urllib.request import urlopen
from pyquery import PyQuery as pq
import shutil as sh

pwd = argv[1]
contest_id = argv[2]
os.makedirs(f"{contest_id}")
os.makedirs(f"{contest_id}/samples")

contest_standings_url = "https://codeforces.com/api/contest.standings"
handles = "lenneo"
contest_standings_params = {
    'contestId': f"{contest_id}",
    'handles': f"{handles}"
}

"""
    This is necessary to get the range of problems within a contest.
    Some contests might have        {A, B, C, D1, D2}
    while another might just have   {A, B, C, D, E, F}
    Therefore, the ranges of problems is contest specific;
"""

request = requests.get(url=contest_standings_url, params=contest_standings_params)

"""
    From the request, need to find the range of problems.
"""
problems = request.json()["result"]["problems"]
problemIdxs = []
for problem in problems:
    problemIdxs.append(problem["index"])

"""
    Given a set of range of problems, query the html page containing the problems.
    Grab the specific problems, and their test cases.
    Then, create the specific problem cpp file to be used.
"""

testData = []

for problemIdx in problemIdxs:
    problemUrl = f"https://codeforces.com/contest/{contest_id}/problem/{problemIdx}"
    problemHtml = urlopen(url=problemUrl)
    #problem_parser = Problem()
    #problem_parser.feed(problemHtml.read().decode())
    pqParser = pq(url=problemUrl,
            opener = lambda url, **kw: urlopen(url).read())
    inputSpec = pqParser('.input-specification').find('p')
    containsMult = inputSpec.text().__contains__("the number of test cases")
    sampleTests = pqParser('.sample-tests')

    # what is needed -> From inside each <pre> within .sample-tests
    #   needed = <pre> -> <div class="input">
    #   needed = <pre> -> <div class="output">
    input = sampleTests.find('.input').find('pre')
    output = sampleTests.find('.output').find('pre')
    testData.append((problemIdx, (containsMult, input.text(), output.text())))

    sh.copyfile("template.cpp", f"{contest_id}/{problemIdx}.cpp")

for testSet in testData:
    prob_idx = testSet[0]
    inputFile = open(f"{contest_id}/samples/{prob_idx}.in", "w")
    outputFile = open(f"{contest_id}/samples/{prob_idx}.out", "w")
    inputFile.write(testSet[1][1])
    outputFile.write(f"{testSet[1][0]}\n")
    outputFile.write(testSet[1][2])
