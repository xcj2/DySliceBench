import sys
from collections import defaultdict, deque
import math

# import copy
from bisect import bisect_left, bisect_right
# import heapq

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
        self.par = [i for i in range(n+1)]
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

    def update(self):
        for i in range(len(self.par)):
            self.par[i] = self.find(i)

def solve():
    n,m = getList()
    nums = getList()
    uf = UnionFind(n)
    for i in range(m):
        x, y = getList()
        uf.union(x, y)
    uf.update()
    st1 = [[] for i in range(n + 1)]
    st2 = [[] for i in range(n + 1)]
    for i in range(n):
        st1[uf.par[i+1]].append(i+1)
        st2[uf.par[i+1]].append(nums[i])

    ans = 0
    for s1, s2 in zip(st1, st2):
        ans += len(list(set(s1) & set(s2)))



    print(ans)
def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()