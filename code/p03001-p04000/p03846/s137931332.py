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
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)

N = _I()
A = LI()

"""
5
2 4 4 0 2

2なら、
xOxxx
xxxOx
の2通りしかない
N=9なら
xxxOxxxxx
xxxxxOxxx
の2通りしかない
4なら
Oxxxxと
xxxxO
しかない
これらをもとに確かめていく


Nが奇数の時
3
2 0 2
とすると成り立つ
4のとき
3 1 1 3
まずこれでできない場合をはじける

計算するまでもないのか。

2 4 4 0 2なら
前か後ろか、前か後ろかをかけるだけなので4

"""
if N == 1:
    if A[0] == 0:
        print(1)
    else:
        print(0)
    exit()

A.sort()

if N % 2 == 0:
    correct = list(range(1, N+1, 2))
    correct = correct + correct
    correct.sort()
else:
    # 奇数時
    correct = list(range(0, N+1, 2))
    correct = correct + correct
    correct.sort()
    correct = correct[1:]
if correct == A:
    ans = 2**(N//2)
    print(ans%mod)
else:
    print(0)
    
