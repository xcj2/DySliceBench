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
    a,b,m = getList()
    anums = getList()
    bnums = getList()
    ans = min(anums) + min(bnums)
    for i in range(m):
        x,y,c = getList()
        tmp = anums[x-1] + bnums[y-1] - c
        if ans > tmp:
            ans = tmp

    print(ans)


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