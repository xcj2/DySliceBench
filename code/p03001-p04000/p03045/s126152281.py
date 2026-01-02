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

# Union-Find木
class UFT:
    def __init__(self, n):
        self.height = [1] * n
        self.group = [-1] * n
    def root(self, v):
        if self.group[v] < 0:
            return v
        self.group[v] = self.root(self.group[v])
        return self.group[v]
    def size(self, v):
        return - self.group[self.root(v)]
    def equal(self, v1, v2):
        v1, v2 = self.root(v1), self.root(v2)
        return v1 == v2
    def merge(self, v1, v2):
        v1, v2 = self.root(v1), self.root(v2)
        if self.equal(v1, v2):
            return False
        if self.height[v1] < self.height[v2]:
            self.group[v2] += self.group[v1]
            self.group[v1] = v2
            self.height[v2] = max(self.height[v1] + 1, self.height[v2])
        else:
            self.group[v1] += self.group[v2]
            self.group[v2] = v1
            self.height[v1] = max(self.height[v1], self.height[v2] + 1)
        return True

# エントリーポイント
def main():
    N, M = input(int, int)
    XYZ = input([[int, 3], M])

    uft = UFT(N + 1)
    for x, y, _ in XYZ:
        uft.merge(x, y)

    cnt = 0
    for t in uft.group[1:]:
        if t < 0:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    args = iter(sys.stdin.read().split())
    main()
