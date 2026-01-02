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
K=read()
mod=7%K
index=1
dic=defaultdict(int)
while(True):
    if mod==0:
        print(index)
        exit()
    if dic[mod]==1:
        print(-1)
        exit()
    dic[mod]=1
    mod=mod*10+7
    mod%=K
    index+=1
    