def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return list(input())
#UnionFindクラス
class UnionFind(object):
 
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.size=[1 for i in range(n)]
 
    def find(self, x):
  
        if self.par[x] == x:
            return x
        else:
            return self.find(self.par[x])
  
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
            self.size[x]+=self.size[y]
  # x,yの根が同じかどうかを返す（根が同じ:True、根が異なる:False）
    def same(self, x, y):
        return self.find(x) == self.find(y)

    
n,m=IL()
l=[[0,0] for i in range(m)]
par=[1 for i in range(n)]
for i in range(m):
    a,b=IL()
    l[i]=[a-1,b-1]
ans=[0 for i in range(m)]
uf=UnionFind(n)
t_ans=n*(n-1)/2
ans[-1]=t_ans
for i in range(m-1):
    a=uf.find(l[-1-i][0])
    b=uf.find(l[-1-i][1])
    
    if a!=b:
        t_ans-=uf.size[a]*uf.size[b]
        uf.union(a,b)
    ans[-2-i]=t_ans
for i in range(m):
    print(int(ans[i]))