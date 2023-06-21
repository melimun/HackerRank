#An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:
# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
#steps = 8 path = [DDUUUUDD]

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#+1 -3 +1 -1 +2
# U DDD U D UU
# if there

def countingValleys(steps, path): 
    sea_level = 0
    numOfValley = 0
  
    for step in path:
        if step == 'U':
            sea_level += 1
        else:
            sea_level -= 1
    
        if step == 'U' and sea_level == 0:
            numOfValley+=1
    
    return numOfValley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
