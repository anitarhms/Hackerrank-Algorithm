#subarray division
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    n=len(s)
    hasil=0
    #m=2 s=5 -> x= 4 
    #m=3 s=5 -> x=3     maka x = s-m+1
    
    for i in range (0,n-m+1): 
        if sum(s[i:i+m])==d:  #slicing untuk len(s)=5 dan m=2 adalah s[0:2][1:3][2:4][3:5] jadi s[i:i+m]
            hasil+=1
    return hasil

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
