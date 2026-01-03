import sys
sys.setrecursionlimit(1000000)
from math import factorial, ceil, floor
from bisect import bisect_right as bsr
from operator import itemgetter as ig
from collections import defaultdict as dd
from collections import deque, Counter as cnt

# お約束
args = None
INF = float("inf")
MOD = int(1e9 + 7)
def input(*ps):
    if type(ps[0]) is list:
        return [input(*ps[0][:-1]) for _ in range(ps[0][-1])]
    elif len(ps) == 1:
        return ps[0](next(args))
    else:
        return [p(next(args)) for p in ps]
def nlist(n, v):
    if not n: return v.copy()
    return [nlist(n[1:], v) for _ in range(n[0])]

# バイナリインデックス木
class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
    def sum(self, i):
        s = 0
        while 0 < i:
            s += self.tree[i]
            s %= MOD
            i -= i & -i
        return s
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

# エントリーポイント
def main():
    N, T = input(int, int)
    A = input([int, N])

    ans = 0
    for n in range(N - 1):
        ans += min(T, A[n + 1] - A[n])
    print(ans + T)

if __name__ == '__main__':
    args = iter(sys.stdin.read().split())
    main()
