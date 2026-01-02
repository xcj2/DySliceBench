import sys
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
N, K = IL()
r, s, p = IL()
t = S()

judge = {'r':p,'s':r,'p':s}

ans = 0
for i in range(N):
  ans += judge[t[i]]

for n in range(K):
  tmp = ''
  cnt = 0
  for i in range(n,N,K):
    if t[i] == tmp:
      cnt += 1
    else:
      if tmp != '':
        ans -= judge[tmp] * (cnt//2)
      tmp = t[i]
      cnt = 1
  else:
    if tmp != '':
      ans -= judge[tmp] * (cnt//2)

print(ans)