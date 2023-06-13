#Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

#STDIN           Function
# -----           --------
# 6               arr[] size n = 6
# -4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

#OUTPUT (ratio of how many above 1, at 0 and below 0 there are)
#0.500000
#0.333333
#0.166667

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    neg = 0 
    zero = 0
    
    n = len(arr)
    
    for i in arr:
        if i == 0:
            zero+=1
        elif i<0:
            neg+=1
        elif i>=1:
            pos+=1
    
    print(f'{pos/n:.6f}')
    print(f'{neg/n:.6f}')
    print(f'{zero/n:.6f}') 

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
