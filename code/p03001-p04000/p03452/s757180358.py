class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n+1)]  # 親のノード番号
        self.rank = [0]*(n+1)
        self.diff_weight = [0]*(n+1)  # 親ノードとのweightの差
    def root(self,x):  # xの根のノード番号
        if self.par[x] == x:
            return x
        else:
            r = self.root(self.par[x])
            self.diff_weight[x] += self.diff_weight[self.par[x]]
            self.par[x] = r
            return self.par[x]
    def same_check(self,x,y):  # x,yが同じグループか否か
        return self.root(x) == self.root(y)
    def weight(self,x):
        r = self.root(x)  # 経路圧縮
        return self.diff_weight[x]
    def diff(self,x,y):
        return self.weight(y) - self.weight(x)
    def unite(self,x,y,w):  # x,yの属するグループの併合
        w += self.weight(x)
        w -= self.weight(y)
        x = self.root(x)
        y = self.root(y)
        if self.rank[x] < self.rank[y]:
            x,y = y,x
            w = -w
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x
        self.diff_weight[y] = w

import sys

sys.setrecursionlimit(10**7)
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def S(): return sys.stdin.readline().rstrip()

N,M = map(int,S().split())
G = UnionFind(N)
for i in range(M):
    L,R,D = LI()
    if G.same_check(L,R):
        if G.diff(L,R) != D:
            print('No')
            exit()
    else:
        G.unite(L,R,D)

print('Yes')