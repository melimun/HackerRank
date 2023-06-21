# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  

# difference is 15-17=2
# primary diagonal sum is 15 and secondary diagonal sum is 17 (left to right + right to left)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#11 2 4
#4 5 6
#10 8 -12

#arr[0][0] arr[0][1] arr[0][2]
#arr[1][0] arr[1][1] arr[1][2]
#arr[2][0] arr[2][1] arr[2][2]

#primary diagonal is arr[0][0] + arr[1][1] + arr[2][2]
#secondary diagonal is arr[2][0] + arr[1][1] + ar[0][2]

def diagonalDifference(arr):
   # Initialize sums of diagonals
   d1 = 0
   d2 = 0

   for i in range(0, n):
    
       for j in range(0, n):
        
           # finding sum of primary diagonal
           if (i == j):
               d1 += arr[i][j]

           # finding sum of secondary diagonal
           if (i == n - j - 1):
               d2 += arr[i][j]
        
   # Absolute difference of the sums
   # across the diagonals
   return abs(d1 - d2);
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
