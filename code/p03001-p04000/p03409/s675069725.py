import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def pf(s): return print(s, flush=True)

N = I()
A,B = [], []
for n in range(N):
    A.append(LI())
for n in range(N):
    B.append(LI())

#  N = 100
#  A,B = [], []
#  for n in range(N):
#      A.append([random.randint(0,2*N), random.randint(0, 2*N)])
#  for n in range(N):
#      B.append([random.randint(0,2*N), random.randint(0, 2*N)])

B = sorted(B, key=lambda x: x[0])

result = 0
for b in B:
    tmp = [a for a in A if a[0] < b[0] and a[1] < b[1]]
    if not tmp:
        continue
    result += 1
    closest = max(tmp, key=lambda x: x[1])
    A.remove(closest)
print(result)

