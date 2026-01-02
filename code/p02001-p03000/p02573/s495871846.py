from sys import stdin, setrecursionlimit
from collections import Counter, deque, defaultdict
from math import floor, ceil
from bisect import bisect_left
from itertools import combinations
setrecursionlimit(100000)

class UnionFind(object):
    def __init__(self, n):
        self.par = [-1] * n
    
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return False
        else:
            if self.par[x] > self.par[y]:
                x, y = y, x
            self.par[x] += self.par[y]
            self.par[y] = x
            return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        return len(self.roots())

def main():
    from builtins import int, map
    N, M = map(int, input().split())
    uf = UnionFind(N)
    for _ in range(M):
        ai, bi = map(lambda x: int(x) - 1, input().split())
        uf.unite(ai, bi)

    # 最大のグループサイズ
    ans = -1
    for n in range(N):
        ans = max(ans, uf.size(n))
        # print(n, uf.size(n))
    print(ans)

if __name__ == '__main__':
    main()