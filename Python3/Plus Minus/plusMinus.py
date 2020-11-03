#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr)
    plus = 0
    minus = 0
    zero = 0
    
    for i in range(length):
        if (arr[i] > 0):
            plus += 1
        elif (arr[i] < 0):
            minus += 1
        else:
            zero += 1
    prPlus = plus/length
    prMinus = minus/length
    prZero = zero/length
    
    print('%.6f' % prPlus)
    print('%.6f' % prMinus)
    print('%.6f' % prZero)
    
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
