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
    N, K = input(int, int)
    A = input([int, N])

    MAX = 2010
    bit = BIT(MAX)
    # 最終周をカウントする
    sum1 = []
    for i, a in enumerate(A, start=1):
        bit.add(a, 1)
        sum1.append(i - bit.sum(a))
    # 繰り返し周をカウントする
    sum2 = []
    for a in A:
        sum2.append(N - bit.sum(a))
    # (1 + (K - 1))回分を集計する
    ans = 0
    for v1, v2 in zip(sum1, sum2):
        ans += K * v1 + ((K * (K - 1)) // 2) * v2
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    args = iter(sys.stdin.read().split())
    main()
