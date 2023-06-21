# You will be given a list of 32 bit unsigned integers. Flip all the bits ( and ) and return the result as an unsigned integer.

# Sample Input
# The first line of the input contains , the number of queries.
# Each of the next  lines contain an integer, , to process.

# 3 
# 2147483647 
# 1 
# 0

# Sample Output

# 2147483648 
# 4294967294 
# 4294967295


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    bit = '{0:032b}'.format(n)
    inverse = ''
    
    for num in bit:
        if num == '0':
            inverse+='1'
        if num == '1':
            inverse+='0'
    
    return int(inverse,2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

