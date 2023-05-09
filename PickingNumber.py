#picking number ver1
from collections import Counter
s=[1,2,2,3,1,2]
y=[4, 6 ,5 ,3, 3, 1]
arr=Counter(s)
maxi=0
for i in range (1,100):
  maxi=max(maxi, arr[i]+arr[i+1])
print (maxi)

#picking number ver2
unik=sorted(set(s))
n_max= max([s.count(bil) for bil in unik])

for x,y in zip(unik[:-1],unik[1:]):
  if abs (x-y) not in (0,1):
     continue
  n=s.count(x)+s.count(y)
  n_max=max(n_max,n)
print('hasil= ',n_max)
