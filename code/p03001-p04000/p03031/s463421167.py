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

N, M = LI()
S = [LI()[1:] for i in range(M)]
ps = LI()

"""
何通りあるか
10までの制限なので、軽い
すべてのスイッチの通りは、2*10=1024通り
それぞれの場合について、最大10個見ればいいのでかんたん

"""
ans = 0
def dfs(sidx, switches):
    global ans
    # onの場合とoffの場合を検証していく
    if sidx == N:
        # 全スイッチの状態を決定できたので、判定する
        #  print('swi' , switches)
        for sidx, s in enumerate(S):
            # sはスイッチのリスト
            v = sum([switches[i-1] for i in s]) % 2
            if v == ps[sidx]:
                # ついてる
                pass
            else:
                # ついてないので止める
                return
        else:
            ans += 1
    else:
        dfs(sidx+1, switches + [0])
        dfs(sidx+1, switches + [1])
dfs(0, [])
print(ans)
