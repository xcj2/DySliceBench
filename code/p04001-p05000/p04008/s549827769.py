# coding:utf-8

import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n, k = LI()
    A = LI_()

    D = defaultdict(list)
    for i in range(1, n):
        D[A[i]].append(i)

    # 首都は必ず自己ループでなければならない
    global res
    res = 0 if A[0] == 0 else 1

    def DFS(v, par):
        global res
        h = 0
        for to in D[v]:
            # print('dfs {} -> {}'.format(v+1, to+1))
            # h: 葉からの距離の最大値
            h = max(h, DFS(to, v))

        # 根が首都ではなく，高さがk - 1の場合は首都につなぎ直す
        if h == k - 1 and par != 0:
            res += 1
            h = -1
        # print('Finish {} <- {}'.format(par+1, v+1))
        return h + 1

    DFS(0, 0)

    return res


print(main())
