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
#s=["" for i in range(n)]
ac,wa,tle,re=0,0,0,0
for i in range(n):
  s=input()
  if s=="AC":
    ac+=1
  elif s=="WA":
    wa+=1
  elif s=="TLE":
    tle+=1
  else :
    re+=1
print("AC x "+ str(ac) )
print("WA x "+ str(wa) )
print("TLE x "+ str(tle) )
print("RE x "+ str(re) )

