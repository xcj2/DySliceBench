def getN():
    return int(input())

def getMN():
    a = input().split()
    b = [int(i) for i in a]
    return b[0],b[1]

def getlist():
    a = input().split()
    b = [int(i) for i in a]
    return b

from collections import Counter
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1 for i in range(n)]
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
            self.size[y] += self.size[x]
            self.size[x] = 0
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.size[x] += self.size[y]
            self.size[y] = 0

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)



n,m = getMN()

bridges = []

for i in range(m):
    a,b = getMN()
    bridges.append([a,b])

bridges.reverse()

uf = UnionFind(n)
ans = n*(n-1)//2
answers = [ans]
for query in bridges:
    x,y = query
    if not uf.same_check(x-1,y-1):
        #print(uf.size,x,y)
        ans -= uf.size[uf.find(x-1)]*uf.size[uf.find(y-1)]
        #print(uf.find(x-1))
        uf.union(x-1,y-1)

    answers.append(ans)

for fa in answers[:-1][::-1]:
    print(fa)
