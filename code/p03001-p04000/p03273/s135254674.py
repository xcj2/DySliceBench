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
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    H, W = LI()
    A = []
    [A.append(S()) for i in range(H)]

    # まず横向きで削除していく
    rm_idx = []
    for idx, a in enumerate(A):
        if '#' not in a:
            rm_idx.append(idx)

    count = 0
    for idx, i in enumerate(rm_idx):
        del A[i-count]
        count += 1

    # 縦向きに探索
    rm_idx = []
    for w in range(W):
        if all(a[w] == '.' for a in A):
            rm_idx.append(w)

    count = 0
    for idx, i in enumerate(rm_idx):
        A = [a[:i-count] + a[i-count+1:] for a in A]
        count += 1

    for a in A:
        print(''.join(a))


if __name__ == "__main__":
    main()
