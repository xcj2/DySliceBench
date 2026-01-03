import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
from fractions import Fraction
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
TA = [LI() for _ in range(N)]
"""
まず割合を求める
割合が違ったら数字を変更する必要がある
2:1にしないといけないのに
10-20
だったら、
答えは40-20であるが、
2:1をまず10-20より大きくする
まず割る
10/2=5
20/1=20
だからまず20倍する
40:20
これが答えであればok
逆ならどうか
17:25
2-3
なら
そもそも17:25が正解
じゃあ一方だけこえてたら？
17:25
21-3
これなら
まず小さい方は25にする
21-25
そこから割合を求める
21/17=1....
25/25 = 1
2倍する
34:50
満たしている
"""

vals = [1,1]
for t, a in TA:
    #  # まず同じ大きさにする
    #  if vals[0] < t:
    #      vals[0] = t
    #  if vals[1] < a:
    #      vals[1] = a

    xt = math.ceil(Fraction(vals[0], t))
    xa = math.ceil(Fraction(vals[1] , a))

    max_x = max(xt, xa)
    #  t *= max_x
    #  a *= max_x
    vals[0] = t * max_x
    vals[1] = a * max_x

print(sum(vals))
