import math, string, itertools, fractions, heapq, collections, re, \
array, bisect, sys, random, time, copy, functools, os, queue, pdb
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
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)

N, K = LI()
A = LI()

from fractions import Fraction
"""
2 1なら
2 1 2 1
点灯数は、左の数のほうが多いもの
2 1
2 1
2 1
の3種類
2回つなげてみたら決まる
2 1 2 1なら
K = 2で3
K=3 で 2 1 2 1 2 1で6
K=4 で2 1 2 1 2 1 2 1で10通り 4+3+2+1=
K=6なら 2 1 2 1 2 1 2 1 2 1 2 1で6+5+4+3+2+1 =

偶奇でわける
modで割る

1 2なら
1 2 1 2で1しかない1
1 2 1 2 1 2なら3で2 + 1
1 2 1 2 1 2 1 2 なら6で3+2+1
"""
if len(set(A)) == 1:
    print(0)
    exit()

"""
各数字ごとに数える
"""
K %= mod
in_count = 0
for i in range(N):
    for j in range(i, N):
        if A[i] > A[j]:
            #  print('i, j', i,j, A[i], A[j])
            in_count += 1
#  print(in_count)
in_count %= mod
in_ans = in_count * K
in_ans %= mod

out_count = 0
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            out_count += 1
#  print(out_count)

out_count %= mod
#  out_ans = (out_count * K * (K-1))//2
#  out_ans = out_count * (((K * (K-1))%mod)/2) % mod
out_ans = int(Fraction(out_count) * Fraction(K) * Fraction(K-1) / Fraction(2))
out_ans %= mod
#  print(in_ans, out_ans)
print(int((in_ans + out_ans)%mod))
