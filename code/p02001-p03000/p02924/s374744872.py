import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, os, pdb
sys.setrecursionlimit(10**7)
from fractions import Fraction
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
def perr(s): return print(s, file=sys.stderr)

N = _I()

"""
並び替えた後あまりを計算する
まずは貪欲的に考える
大きい方からあまりが最大になるものをマッチングする
しかしこれだと10**9なので絶対間に合わない
gcdとかいきてきそう
そもそもあまりが
1,2,...Nを割っていく
Nを割ってN余ることはない。
8 % 9は8になる。
ひとつずつずらしていくか
そうすると、1/2n n+1がなりたつ
"""

ans = Fraction(1/2) * Fraction(N) * Fraction(N-1)
print(int(ans))
