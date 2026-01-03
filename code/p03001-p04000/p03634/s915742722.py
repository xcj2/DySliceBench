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


# --------------------------------------------

dp = None
D = None
D_dfs_d = None


def dfs_d(v, pre, dist):
    global D_dfs_d

    D_dfs_d[v] = dist

    for next_v, d in D[v]:
        if next_v != pre:
            dfs_d(next_v, v, dist + d)

    return


def main():
    global D
    global D_dfs_d

    N = int(input())
    D_dfs_d = [-1] * (N + 1)
    D = [[] for _ in range(N + 1)]

    for i in range(N - 1):
        a, b, c = li_input()
        D[a].append((b, c))
        D[b].append((a, c))

    Q, K = li_input()

    # Kから各頂点までの長さをWFSで求める
    dfs_d(K, -1, 0)

    for i in range(Q):
        x, y = li_input()
        print(D_dfs_d[x] + D_dfs_d[y])


main()
