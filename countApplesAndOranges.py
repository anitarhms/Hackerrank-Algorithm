#menghitung jumlah apel dan jeruk yang jatuh di pekarangan rumah 
#misal pada x axis, pohon apel (a) = 4, pohon jeruk (b)=12. letak rumah pada nilai 7 hingga 10
#ada masing masing 3 buah apel dan jeruk yang jatuh. Nilai d menunjukan jarak jatuhnya buah dari pohonnya. 
#nilai d negatif berarti buah jatuh sejauh d unit ke kiri pohon, sedangkan d positif jatuh sejauh d unit ke kanan pohon 
#Buah jatuh pada nilai d: apel [2,3,-4] dan jeruk [3,-2,-4]

#sehingga solusinya : posisi buah jatuh + letak pohon. Bila dalam range letak rumah berarti termasuk
#apel [2+4,3+4,-4+4] = [6,7,0] -> ada 1 apel yg jatuh di pekarangan



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    jml_apel=0
    jml_org=0
    for i in range (len(apples)):
        jatuh= a+apples[i]
        if jatuh in range (s,t+1):
            jml_apel+=1
    for i in range (len(oranges)):
        jatuh= b+oranges[i]
        if jatuh in range (s,t+1):
            jml_org+=1
    print (jml_apel)
    print (jml_org)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
