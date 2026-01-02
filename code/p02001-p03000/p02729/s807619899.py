import sys; sys.setrecursionlimit(2147483647); input = sys.stdin.readline
from math import floor, ceil, sqrt, factorial, log
from collections import Counter, defaultdict, deque
from operator import itemgetter
INF = float('inf'); MOD = 10**9+7
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(MI())
def LIR(n): return [LI() for i in range(n)]
def IS(): return input().rstrip()
from operator import mul
from functools import reduce

def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


def main():
    N, M = MI()
    if N > 1:
        n = combinations_count(N, 2)
    else:
        n = 0
    if M > 1:
        m = combinations_count(M, 2)
    else:
        m = 0
    print(n+m)

if __name__ == '__main__':
    main()