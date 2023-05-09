from collections import Counter
n=int(input())
ar= list(map(int,input().split()))
c=Counter(ar)
jml=list(c.values())
pasang=0
for i in range (len(jml)):
    if jml[i]%2 == 0 and jml[i]>1 :
        pasang+= (jml[i]//2)
    if jml[i]%2 !=0 and jml[i]>1:
        pasang+=(jml[i]//2)
print (pasang)
