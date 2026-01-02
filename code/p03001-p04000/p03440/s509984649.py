import sys
from collections import defaultdict, deque, Counter
import math

# import copy
from bisect import bisect_left, bisect_right
import heapq

# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline

getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = 10 ** 20
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * (n+1)

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
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

def main():
    n, m = getList()
    uf = UnionFind(n)
    costs = getList()

    q = []
    for i, c in enumerate(costs):
        heapq.heappush(q, (c, i))
    # print(q)
    hen = 0
    for _ in range(m):
        a, b = getList()
        if not uf.same_check(a, b):
            uf.union(a,b)
            hen += 1
 
    # print(uf.par)
    ans = 0
    used = defaultdict(int)
    kaburi = []
    mc = 0
    while(q):
        c1, m1 = heapq.heappop(q)
        if uf.find(m1) not in used.keys():
            ans += c1
            used[uf.find(m1)] = 1
            mc += 1
        else:
            heapq.heappush(kaburi, (c1, m1))

    # print(kaburi, hen, ans)
    if mc == 1:
        print(0)
        return 

    if len(kaburi) >= 2 * (n - hen - 1) - mc:
        for _ in range(2 * (n - hen - 1) - mc):
            c1, m1 = heapq.heappop(kaburi)
            ans += c1
        print(ans)
        return 
    else:
        print("Impossible")
        return


if __name__ == "__main__":
    main()
    # solve()

