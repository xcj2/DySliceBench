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

N = I()
s = S()

ans = 0
for i in range(10):
  for j in range(10):
    for k in range(10):
      num = str(i) + str(j) + str(k)
      st = 0
      for n in num:
        for x in range(st, N):
          if s[x] == n:
            st = x+1
            break
        else:
          break
      else:
        ans += 1

print(ans)