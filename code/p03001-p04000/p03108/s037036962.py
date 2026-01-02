import sys
import math
from collections import defaultdict, deque, Counter
from copy import deepcopy
from bisect import bisect, bisect_right, bisect_left
from heapq import heapify, heappop, heappush
    
input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def TI(): return tuple(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]

class UnionFind():
    """
    要素数nで初期化
    """
    
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
        """
        union(x, y)でx, yをグルーピング
        """
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
        """
        same(x, y)同じグループに属しているか
        """
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
    N, M = MI()
    Union = UnionFind(N)
    Num = N*(N-1) // 2
    res = [0]*M
    res[0] = Num
    L = [LI() for i in range(M)]
    
    for index, l in enumerate(reversed(L[1:])):
        a, b = l
        if not Union.same(a-1, b-1):
            res[index+1] -= Union.size(a-1) * Union.size(b-1)
        res[index+1] += res[index]
        Union.union(a-1, b-1)
        if res[index+1] == 0:
            break

    for i in reversed(res):
        print(i)
    
if __name__ == "__main__":
    main()