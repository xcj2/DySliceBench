"""
unite時に矛盾しないかどうかを判定させる。
同じ木の中では、より右にいるノードを親とする。
親との距離をどこかに記録しておく。
"""
class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parents = [i for i in range(n+1)]
        self.dict = [0]*(N+1)
    def find(self,x):
        if self.parents[x]==x:
            return x
        else:
            self.find(self.parents[x])
            u = self.dict[self.parents[x]]
            self.parents[x]=self.find(self.parents[x])
            #xのdictを更新する。
            self.dict[x] += u
            return self.parents[x]
    def unite(self,x,y,d):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            if self.dict[x]-self.dict[y]!=d:
                print("No")
                exit()
        #より右にいるノードを親にする
        if self.dict[y]+d > self.dict[x]:
            self.parents[xRoot] = yRoot
            self.dict[xRoot] = self.dict[y]+d-self.dict[x]
        else:
            self.parents[yRoot] = xRoot
            self.dict[yRoot] = self.dict[x]-(self.dict[y]+d)

N,M = map(int,input().split())
tree = UnionFind(N)
for _ in range(M):
    l,r,d = map(int,input().split())
    tree.unite(l,r,d)
print("Yes")