import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)
#read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def read():
  return int(readline())
def reads():
  return map(int, readline().split())
def mp(arg):
  return map(int,arg.split())

n,m=reads()
link=[[]for i in range(n)]
for i in range(m):
  x,y=reads()
  link[x-1].append(y-1)
#print(link)
@lru_cache(None)
def dp(k):
  res=0
  for ele in link[k]:
    res=max(res,dp(ele)+1)
  return res
res=1
for i in range(n)  :
  res=max(res,dp(i))
print(res)