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
    global a, p
    N, X = LI()
    #  N = 50
    #  X = 4321098765432109
    a, p = [1], [1]
    for i in range(N):
        a.append(a[i] * 2 + 3)
        p.append(p[i] * 2 + 1)
    print(make_burger(N, X))
    return


def make_burger(N, X):
    if N == 0:
        return 0 if X <= 0 else 1
    elif X <= 1 + a[N-1]:
        return make_burger(N-1, X-1)
    elif X == 2 + a[N-1]:
        return p[N-1] + 1
    elif X <= 2 + 2*a[N-1]:
        return p[N-1] + 1 + make_burger(N-1, X - 2 - a[N-1])
    else:
        return 2*p[N-1] + 1


if __name__ == '__main__':
    main()
