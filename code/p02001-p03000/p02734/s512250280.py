import sys
from functools import lru_cache
 
#read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**6)
def read():
  return int(readline())
def reads():
  return map(int, readline().split())
def mp(arg):
  return map(int,arg.split())
n,s=reads()
a=list(reads())
mod= 998244353
f=[[] for i in range(n+1)]
for k in range(1,n+1):
  if k==1:
    res=[0]*(s+1)
    res[0]=1
    if a[0]<s+1:
      res[a[0]]=1
    f[1]=res
    continue
  res=f[k-1][:]
  k-=1
  for i in range(s,-1,-1):
    if i-a[k]>=0:
      res[i]+=res[i-a[k]]
      res[i]%=mod
  if a[k]<s+1:
      res[a[k]]+=1
  res[0]+=1
  f[k+1]=res
ans=0
#print(f)
for i in range(1,n+1):
  ans+=f[i][-1]
ans%=mod
print(ans)