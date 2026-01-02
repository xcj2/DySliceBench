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
A = LI()
"""
i番目を抜く時、iとi-1,iとi+1の距離を全体から引いて、そこにi-1とi+1の距離を足す
"""
A = [0] + A + [0]
total = 0
diff1 = []
diff2 = []
for aidx in range(len(A)):
    if aidx == 0:
        continue
    total += abs(A[aidx]-A[aidx-1])
    if aidx == len(A)-1:
        break
    diff1.append(abs(A[aidx] - A[aidx-1])+abs(A[aidx+1] - A[aidx]))
    diff2.append(abs(A[aidx-1] - A[aidx+1]))
#  print(total, diff1, diff2)
for aidx in range(N):
    print(total-diff1[aidx]+diff2[aidx])
