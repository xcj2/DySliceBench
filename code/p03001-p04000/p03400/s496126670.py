import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def SS(): return map(str,sys.stdin.readline().rstrip().split())
def II(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
D,X = II()
A = [I() for _ in range(N)]

for a in A:
  cnt = 0
  d = 1
  while True:
    if D >= d:
      cnt += 1
      d += a
    else:
      break
  X += cnt
print(X)