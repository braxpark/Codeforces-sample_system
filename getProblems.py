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

print(problemIdxs)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    "Content-Type": "application/json",
    "Sec-Ch-Ua": "\"Chromium\";v=\"129\", \" Not A;Brand\";v=\"8\"",
}

for problemIdx in problemIdxs:
    problemUrl = f"https://codeforces.com/contest/{contest_id}/problem/{problemIdx}"
    print(f"Getting problem {problemIdx} from {problemUrl}")
    problemHtml = requests.get(url=problemUrl, headers=headers).text
    doc = pq(problemHtml)
    iS = doc('.sample-tests').find('.input').find('pre').text()
    oS = doc('.sample-tests').find('.output').find('pre').text()
    testData.append(( problemIdx, (oS, iS)))
    sh.copyfile("template.cpp", f"{contest_id}/{problemIdx}.cpp")

for testSet in testData:
    prob_idx = testSet[0]
    inputFile = open(f"{contest_id}/samples/{prob_idx}.in", "w")
    outputFile = open(f"{contest_id}/samples/{prob_idx}.out", "w")
    inputFile.write(f"{testSet[1][1]}\n")
    outputFile.write(f"{testSet[1][0]}\n")
