import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from  collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
    N, M, K = MI()
    uf = UnionFind(N)
    fri_list = [[]for _ in range(N)]
    blo_list = [[]for _ in range(N)]
    cnt_list = [0] * N
    for i in range(M):
        a, b = MI()
        a, b = a - 1, b - 1
        uf.union(a, b)
        fri_list[a].append(b)
        fri_list[b].append(a)
    for i in range(K):
        c, d = MI()
        c, d = c - 1, d - 1
        blo_list[c].append(d)
        blo_list[d].append(c)
    for i in range(N):
        cnt = uf.size(i)
        cnt -= len(fri_list[i]) + 1
        for b in blo_list[i]:
            if uf.same(i, b) == True:
                cnt -= 1
        cnt_list[i] = cnt
    print(' '.join(map(str, cnt_list)))


if __name__ == "__main__":
    main()
