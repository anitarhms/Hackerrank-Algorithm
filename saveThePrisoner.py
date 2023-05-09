#save the prisoner
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

def saveThePrisoner(n, m, s):
    # Write your code here
    # n=4 m=6 s=2      2 3 4 1 2 3
    # n=3 m=7 s=3      3 1 2 3 1 2 3 
    ans=(s+m-1) #7 dan 9 
    ans=ans%n   #7%4=3  9%3=0
    if ans==0:
        return n
    else:
        return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
