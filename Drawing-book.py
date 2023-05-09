#Drawing book
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    front = p//2 #misal p=3 jadi 3//2 = 1 5//2=2
    if n%2==0 : #kalau page genap misal 6, (n-p)//2 = (6-5)//2= 0 maka agar bisa jd 1 -> (n-p+1)//2 
        back= (n-p+1)//2
    else:
        back= (n-p)//2
    return min(front,back)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()