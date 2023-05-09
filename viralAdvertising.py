#viral advertising
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#pada day 1, share= 5, sehingga like = (5//2)=2, kemudian 2 orang yg ngelike itu masing-masing ngeshare ke 3 orang temannya, 
#sehingga pada day 2, share=2*3=6, dan dari 6 orang yg ngeshare, setengahnya ngelike. begitu seterusnya

def viralAdvertising(n):
    # Write your code here
    jumlahlike=0
    shared=5
    for i in range(n):
        like=shared//2
        jumlahlike+=like
        shared=like*3
    return jumlahlike
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
