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

from collections import defaultdict

n,k,l=map(int,input().split())
load=UnionFind(n)
train=UnionFind(n)
for i in range(k):
    a,b=map(int,input().split())
    load.union(a,b)
for i in range(l):
    a,b=map(int,input().split())
    train.union(a,b)

ar=[(load.find(i),train.find(i)) for i in range(1,n+1)]
dic=defaultdict(int)

for i in ar:
    dic[i]+=1

ans=[]
for i in range(n):
    ans.append(dic[ar[i]])
print(*ans)

    