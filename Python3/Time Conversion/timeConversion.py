#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time = ""
    
    if(s[-2:] == "PM"):
        if(int(s[0:2]) < 12):
            time = time + str(12 + int(s[0:2])) + s[2:-2]
        else:
            time = time + str(int(s[0:2])) + s[2:-2]
    else:
        if(s[0:2] == '12'):
            time = time + "00" + s[2:-2]
        else:
            time = time + s[:-2]
    return time
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
