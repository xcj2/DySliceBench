import sys
import math
import collections
import itertools
import array
import inspect

# Set max recursion limit
sys.setrecursionlimit(1000000)


# Debug output
def chkprint(*args):
    names = {
        id(v): k
        for k, v in inspect.currentframe().f_back.f_locals.items()
    }
    print(', '.join(
        names.get(id(arg), '???') + ' = ' + repr(arg) for arg in args))


# Binary converter
def to_bin(x):
    return bin(x)[2:]


def li_input():
    return [int(_) for _ in input().split()]


def gcd(n, m):
    if n % m == 0:
        return m
    else:
        return gcd(m, n % m)


def gcd_list(L):
    v = L[0]

    for i in range(1, len(L)):
        v = gcd(v, L[i])

    return v


def lcm(n, m):
    return (n * m) // gcd(n, m)


def lcm_list(L):
    v = L[0]

    for i in range(1, len(L)):
        v = lcm(v, L[i])

    return v


# Width First Search (+ Distance)
def wfs_d(D, N, K):
    """
    D: 隣接行列(距離付き)
    N: ノード数
    K: 始点ノード
    """

    dfk = [-1] * (N + 1)
    dfk[K] = 0

    cps = [(K, 0)]
    r = [False] * (N + 1)
    r[K] = True
    while len(cps) != 0:
        n_cps = []
        for cp, cd in cps:
            for i, dfcp in enumerate(D[cp]):
                if dfcp != -1 and not r[i]:
                    dfk[i] = cd + dfcp
                    n_cps.append((i, cd + dfcp))
                    r[i] = True

        cps = n_cps[:]

    return dfk


# Depth First Search (+Distance)
def dfs_d(v, pre, dist):
    """
    v:  現在のノード
    pre: １つ前のノード
    dist: 現在の距離

    以下は別途用意する
    D: 隣接リスト(行列ではない)
    D_dfs_d: dfs_d関数で用いる，始点ノードから見た距離リスト
    """

    global D
    global D_dfs_d

    D_dfs_d[v] = dist

    for next_v, d in D[v]:
        if next_v != pre:
            dfs_d(next_v, v, dist + d)

    return


# --------------------------------------------

dp = None

F_MODE = 1
S_MODE = 2

N = None
D = None
D_from_1, D_from_N = [], []


def dfs(v, prev, depth, mode):
    global D_from_1
    global D_from_N

    for next in D[v]:
        if next != prev:
            if mode == F_MODE:
                D_from_1[next] = depth
            else:
                D_from_N[next] = depth

            dfs(next, v, depth + 1, mode)


def main():
    global D
    global N
    global D_from_1
    global D_from_N

    N = int(input())
    D = [[] for _ in range(N + 1)]

    for i in range(N - 1):
        a, b = li_input()
        D[a].append(b)
        D[b].append(a)

    D_from_1 = [-1] * (N + 1)
    D_from_1[1] = 0
    D_from_N = [-1] * (N + 1)
    D_from_N[N] = 0

    dfs(1, -1, 1, F_MODE)
    dfs(N, -1, 1, S_MODE)

    fennec, snuke = 0, 0

    for i in range(1, N + 1):
        if D_from_1[i] <= D_from_N[i]:
            fennec += 1
        else:
            snuke += 1

    if fennec > snuke:
        print("Fennec")
    else:
        print("Snuke")


main()
