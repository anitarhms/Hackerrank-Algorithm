#compare triplets

a_score = list(map(int,input().split()))
b_score = list(map(int,input().split()))

a_final = 0
b_final = 0
for i in range (3):
  if a_score[i] > b_score[i] :
    a_final +=1
  elif a_score[i] < b_score[i]:
    b_final +=1

print ([a_final,b_final])
