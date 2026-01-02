import sys
import bisect
from functools import lru_cache
from collections import defaultdict
inf = float('inf')
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()
def read():
  return int(readline())
def reads():
  return map(int, readline().split())
n=read()
a=list(reads())
a.sort(reverse=True)
res=a[0]
next=[a[1],a[1]]
k=2
while(True):
  length=len(next)
  hoge=[]
  for i in range(length):
    if k>=n:
      print(res)
      exit()
    res+=next[i]
    hoge.append(a[k])
    hoge.append(a[k])
    k+=1
  next=hoge