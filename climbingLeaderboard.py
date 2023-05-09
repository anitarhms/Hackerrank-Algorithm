#climbing the leaderboard
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    
    ranked = sorted(list(set(ranked)), reverse=True) #nilai unik dan di sort descending 
    player = sorted(player, reverse=True)
    l=len(ranked)
    i=0
    rank_list=[]
    for j in range(len(player)):
        while i<l and player[j]<ranked[i]:
            i+=1
        
        rank_list.append(i+1)
        
    return rank_list[::-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
