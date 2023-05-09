#breaking the records

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
#

def breakingRecords(scores):
    # Write your code here
    n=len(scores) #menghitung panjang skor
    #menhitung banyaknya record high dan low yg dipecahkan
    highcount =0 
    lowcount =0 
    #nilai record terkini untuk masing2 array maxi dan mini 
    maxi=mini=scores[0]
  
    for i in scores :
        if maxi<i:        #jika record tertinggi terkini lebih kecil dari nilai terbaru dalam array skor (ditemukan pecah rekor)
            maxi=i        # rekor terkini diperbaharui
            highcount+=1  # menambah jumlah pecah rekor tertinggi
        if mini>i:        #jika rekor terendah terkini lebih besar dari nilai terbaru dalam array skor (ditemukan nilai yang lebih rendah)
            mini=i        #rekor terendah diperbaharui 
            lowcount+=1   #menambah jumlah pecah rekor terendah

    return highcount,lowcount #mengembalikan jumlah pecah rekor tertinggi, terendah
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
