#075-C
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return input()
#UnionFindクラス
class UnionFind(object):
 
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
 
    def find(self, x):
  
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
  
    # xとyの根を結合させる
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
  
  # x,yの根が同じかどうかを返す（根が同じ:True、根が異なる:False）
    def same(self, x, y):
        return self.find(x) == self.find(y)
n,m=IL()
nl=[]
for i in range(m):
    f,t=IL()
    nl.append([f-1,t-1])
ans=0
for i in range(m):
    uf=UnionFind(n)
    flag=False
    for j in range(m):
        if i==j:
            continue
        uf.union(nl[j][0],nl[j][1])
    nl.append(t)
    for j in range(n):
        for k in range(n):
            if not uf.same(j,k):
                flag=True
    if flag:
        ans+=1
print(ans)