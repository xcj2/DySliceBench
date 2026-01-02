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
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)

N = input()

N = [int(i) for i in N]

def dfs(l):
    if len(l) == 3:
        # 計算する
        result = N[0]
        for idx, op in enumerate(l):
            if op:
                result += N[idx+1]
            else:
                result -= N[idx+1]
        if result == 7:
            s = str(N[0])
            for n in range(len(l)):
                if l[n]:
                    s += "+"
                else:
                    s += "-"
                s += str(N[n+1])
            s += "=7"
            print(s)
            exit()
        return
    dfs(l + [0])
    dfs(l + [1])
dfs([])


