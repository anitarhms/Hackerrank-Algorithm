#Beautiful Days
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#Using the string slicing concept, you can get reverse the string. [::-1] corresponds to [start:stop:step]. When you pass -1 as step, the start point goes to the end and stop at the front.

def beautifulDays(i, j, k):
    # Write your code here
    beautifulday=0
    for day in range (i,j+1): #j+1 agar day terakhir ikut 
        r_day=int(str(day)[::-1])
        if abs(day-r_day)%k==0:
            beautifulday+=1
    return beautifulday
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
