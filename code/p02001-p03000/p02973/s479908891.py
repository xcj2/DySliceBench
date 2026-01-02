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
A = [_I() for i in range(N)]

"""
何個色を使えば塗れるか
最も小さい数字からはじめれば？
最も左からはじめれば？
"""

def bisect(arr, val, cmp):
    l = -1
    r = len(arr)
    while r - l > 1:
        e = (l + r) >> 1
        if cmp(arr[e], val): l = e
        else: r = e
    return r

res = [] 
for a in A:
    #  print('a res', a, res)
    if len(res) == 0:
        res.append(a)
    else:
        if a <= res[-1]:
            # 小さいので追加
            res.append(a)
        else:
            # 入れ替え
            p = bisect(res, a, lambda x, y: x > y)
            if res[p] == a:
                p = bisect(res, a-1, lambda x, y: x > y)
                res[p] = a
            else:
                res[p] = a

print(len(res))
