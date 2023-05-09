#counting valleys 
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
#

def countingValleys(steps, path):
    # Write your code here
    steps=len(path)
    level=valley=0 
    #di sea level, level = 0, kalau ada bukit ('U') level +1, kalau ada lembah level -1 
    for i in path:
        if i == 'U': 
            level+=1
        if i == 'D':
            level-=1
        if level == 0 and i=='U': #harus U karena: level harus bernilai minus dahulu dan jika bertemu 'U' entah berapa kai nilainya menjadi 0
            valley+=1
    return valley
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()


