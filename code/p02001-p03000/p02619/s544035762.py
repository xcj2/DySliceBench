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
d=read()
c=list(reads())
s=[[]for i in range(d) ]
for i in range(d):
    s[i]=list(reads())
t=[[]for i in range(d)]
for i in range(d):
    t[i]=read()
    t[i]-=1
contestcount=26
last=[0 for i in range(contestcount)]
score=0
for i in range(d):
    score+=s[i][t[i]]
    last[t[i]]=i+1
    for j in range(contestcount):
        score-=c[j]*(i+1-last[j])
    print(score)