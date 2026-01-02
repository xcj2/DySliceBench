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
s=[[]for i in range(d)]
for i in range(d):
    s[i]=list(reads())
contestcount=26
last=[0 for i in range(contestcount)]
maxscore=0
backup=()
score=0
for i in range(d):#日にち
  dele=0
  for j in range(contestcount):
        dele-=c[j]*(i+1-last[j])
  for j in range(contestcount):#貪欲法
    hoge=maxscore
    hoge+=s[i][j]
    hoge-=dele
    hoge+=c[j]*(i+1-last[j])
    if hoge>=score:
      backup=(j,last[j])
      score=hoge  
    #print(score,backup)
  maxscore=score
  last[backup[0]]=backup[1]
  print(backup[0]+1)
