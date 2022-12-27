#include <bits/stdc++.h>
using namespace std;
#ifndef __linux__

    #define RESET   "\033[0m"
    #define BLACK   "\033[30m"      /* Black */
    #define RED     "\033[31m"      /* Red */
    #define GREEN   "\033[32m"      /* Green */
    #define YELLOW  "\033[33m"      /* Yellow */
    #define BLUE    "\033[34m"      /* Blue */
    #define MAGENTA "\033[35m"      /* Magenta */
    #define CYAN    "\033[36m"      /* Cyan */
    #define WHITE   "\033[37m"      /* White */
    #define BOLDBLACK   "\033[1m\033[30m"      /* Bold Black */
    #define BOLDRED     "\033[1m\033[31m"      /* Bold Red */
    #define BOLDGREEN   "\033[1m\033[32m"      /* Bold Green */
    #define BOLDYELLOW  "\033[1m\033[33m"      /* Bold Yellow */
    #define BOLDBLUE    "\033[1m\033[34m"      /* Bold Blue */
    #define BOLDMAGENTA "\033[1m\033[35m"      /* Bold Magenta */
    #define BOLDCYAN    "\033[1m\033[36m"      /* Bold Cyan */
    #define BOLDWHITE   "\033[1m\033[37m"      /* Bold White */
#else
    cout << "Windows!";
    #define RESET   ""
    #define BLACK   ""      /* Black */
    #define RED     ""      /* Red */
    #define GREEN   ""      /* Green */
    #define YELLOW  ""      /* Yellow */
    #define BLUE    ""      /* Blue */
    #define MAGENTA ""      /* Magenta */
    #define CYAN    ""      /* Cyan */
    #define WHITE   ""      /* White */
    #define BOLDBLACK   ""      /* Bold Black */
    #define BOLDRED     ""      /* Bold Red */
    #define BOLDGREEN   ""      /* Bold Green */
    #define BOLDYELLOW  ""      /* Bold Yellow */
    #define BOLDBLUE    ""      /* Bold Blue */
    #define BOLDMAGENTA ""      /* Bold Magenta */
    #define BOLDCYAN    ""      /* Bold Cyan */
    #define BOLDWHITE   ""      /* Bold White */
#endif
int main(int argc, char* argv[])
{
    if(argc < 2)
    {
        std::cerr << "Please give a problem number!\n";
    }
    std::string index = argv[1];
    /*
     *  check ex. A.outs  ==  A.out
     */
    std::string problemOutput = "outputs/" + index + ".outs";
    std::string sampleOutput = "samples/" + index + ".out";
    // read program outputs into memory
    // evaluate as strings
    vector<string> programOutputs;
    ifstream infile;
    infile.open(problemOutput);
    while(infile.is_open())
    {
      string line;
      while(getline(infile, line))
      {
        programOutputs.push_back(line);
      }
      infile.close();
    }
    infile.open(sampleOutput);
    string sampleOutputs;
    bool singular = false;
    int count = 0;
    while(infile.is_open())
    {
      string line;
      while(getline(infile, line))
      {
        if(count == 0 && line == "False") singular = true;
        sampleOutputs = line;
        count++;
      }
      infile.close();
    }

    if(programOutputs.size() == 0)
    {
      std::cerr << "No input given. Please redo." << std::endl;
      return -1;
    }

    stringstream sampleStream(sampleOutputs);
    bool allGood = true;
    int num = 0;
    int numPassed = 0;
    cout << "\n\n";
    cout << "Test Cases: Given | Expected" << "\n\n";
    for(auto output : programOutputs)
    {
      string currentCheck;
      sampleStream >> currentCheck;
      cout << BOLDBLACK;
      cout << "Case: ";
      cout << num << ":  " << output << " | " << currentCheck;
      if(output != currentCheck)
      {
        cout << "   FAIL.\n";
        allGood = false;
      }
      else
      {
        cout << "   PASS.\n";
        numPassed++;
      }
      cout << RESET;
      num++;
    }
    cout << "\n\n";
    cout << BOLDRED;
    cout << numPassed << " / " << num << " test cases passed.\n";
    cout << RESET;
    return 0;
}   
