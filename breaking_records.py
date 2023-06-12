# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

# Example

# Scores are in the same order as the games played. She tabulates her results as follows:

#                                      Count
#     Game  Score  Minimum  Maximum   Min Max
#      0      12     12       12       0   0
#      1      24     12       24       0   1
#      2      10     10       24       1   1
#      3      24     10       24       1   1
# Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

# Function Description

# Complete the breakingRecords function in the editor below.

# breakingRecords has the following parameter(s):

# int scores[n]: points scored per game
# Returns

# int[2]: An array with the numbers of times she broke her records. Index  is for breaking most points records, and index  is for breaking least points records.
# Input Format


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.


#Scores
#Input: 12 24 10 24
#Remember the minimum, and remembers the maximum

def breakingRecords(scores):
    minimum = None;
    maximum = None;
    
    record_min = 0;
    record_max = 0;
    
    for i in range(0, len(scores)):
        if not minimum and minimum != 0 or not maximum and maximum != 0:
          minimum = scores[i]
          maximum = scores[i]  
        elif scores[i] < minimum:
            minimum = scores[i]
            record_min+=1
        elif scores[i] > maximum:
            maximum = scores[i]
            record_max+=1
    
    return [record_max, record_min]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
