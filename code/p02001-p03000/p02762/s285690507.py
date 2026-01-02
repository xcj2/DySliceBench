import math
import heapq
import bisect
from collections import defaultdict, Counter, deque
import sys
# input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def update_all(self):
        n = len(self.par)
        for i in range(n):
            self.par[i] = self.find(i)

def main():
    n, m, k = getList()
    friends = [[] for i in range(n)]
    blocks = [[] for i in range(n)]

    uf = UnionFind(n)

    for i in range(m):
        a, b = getList()
        uf.union(a-1, b-1)
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)

    for i in range(k):
        a, b = getList()
        blocks[a-1].append(b-1)
        blocks[b-1].append(a-1)
    uf.update_all()
    # print(uf.par)?
    ans = []
    for i in range(n):
        tmp = uf.size[uf.par[i]]
        for fr in friends[i]:
            if uf.same_check(i, fr):
                tmp -= 1
        for bl in blocks[i]:
            if uf.same_check(i, bl):
                tmp -= 1

        ans.append(tmp-1)

    print(*ans)


if __name__ == "__main__":
    main()

"""
10
203941992 742164984
670850202 743524472
687298546 744891559
676493045 744182895
385467254 742631752
740505911 744926772
425723256 743348462
225362543 742332848
399450535 742706299
563528474 743419738
"""