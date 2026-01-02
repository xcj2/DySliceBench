import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1 for _ in range(n)]

    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.size(root_x) < self.size(root_y):
            root_x, root_y = root_y, root_x
        self.parents[root_x] += self.parents[root_y]
        self.parents[root_y] = root_x
        return True

    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        return root_x == root_y

def main():
    n, q = LI()
    uf = UnionFind(n)
    ans = []
    for _ in range(q):
        com, x, y = LI()
        if com == 0:
            uf.unite(x, y)
        if com == 1:
            if uf.same(x, y):
                ans.append(1)
            else:
                ans.append(0)
    for a in ans:
        print(a)

main()


