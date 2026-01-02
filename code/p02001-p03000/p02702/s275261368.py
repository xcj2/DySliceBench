import sys
import bisect
from functools import lru_cache
from collections import defaultdict
from collections import deque
inf = float('inf')
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()
def read():
  return int(readline())
def reads():
  return map(int, readline().split())
s=input()
n=len(s)
ten=[1]
mod=2019
for i in range(n-1):
  ten.append((ten[i]*10)%mod)
modls=[0]*n
modls[n-1]=int(s[n-1])
dic=defaultdict(int)
dic[modls[n-1]]+=1
dic[0]=1
for i in range(n-2,-1,-1):
  modls[i]=int(s[i])*ten[n-1-i]+modls[i+1]
  modls[i]%=mod
  dic[modls[i]]+=1
ans=0
#print(dic)
for num in dic.values():
	ans+=num*(num-1)//2
#ans+=dic[0]
print(ans)