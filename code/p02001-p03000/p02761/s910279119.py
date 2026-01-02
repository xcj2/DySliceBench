import math
import sys
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N,M = IL()
sc = [SL() for i in range(M)]

if N == 1:
  s = 0
  g = 9
elif N ==2:
  s = 10
  g = 99
else:
  s = 100
  g = 999

for i in range(s,g+1):
  n = str(i)
  for s,c in sc:
    s = int(s)
    if n[s-1] == c:
      continue
    else:
      break
  else:
    print(n)
    exit()
print(-1)