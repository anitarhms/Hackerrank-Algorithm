#circular array 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here
    # [3 4 5] n=3 
    #jika k=1, k%n=1%3=1 dimulai a[-1]=[5] 
    #k=2, 2%3=2 dimulai a[-2]= [4]
    n=len(a)
    k=k%n
    a= a[-k:]+a[:-k] 
    #misal k=1. a[-1:]=[5] a[:-1]=[3,4] -> a=[5,3,4]
    #misal k=2  a[-2:]=[4,5] a[:-2]=[3] -> a= [4,5,3]
    return [a[i] for i in queries] #mengembalikan nilai i di setiap index query 
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
