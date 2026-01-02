import sys
import itertools
import math
from collections import deque
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

#max(chr(ord("z")+1), 
def tami(re,res,cnt,ma):
  if cnt == N:
    ans.append(res)
    return
  for i in range(ord("a"), ma+2):
    tami(chr(i),res+chr(i),cnt+1,max(ma, i))

N = I()

ans = []
tami(chr(ord("a")-1),"",0,ord("a")-1)
ans.sort()
for i in ans:
  print(i)