# Given an array of integers and a positive integer k , determine the number of (i,j) pairs where i<j and  ar[j]+ar[i] is divisible by k.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    pairs = [] 
    
    for i in range(0, n):
        for j in range(1, n):  
            if (i<j) and ((ar[i] + ar[j]) % k == 0):
                pairs.append([ar[i], ar[j]])  
    print(pairs)
    return len(pairs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
