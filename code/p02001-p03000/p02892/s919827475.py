n=int(input())
l=[[j for j,k in enumerate(input())if k=="1"]for i in range(n)]
class UnionFind:
    #def   -> foo=UnionFind(n,1)  <- 1-based index, default is 0
    #method -> foo.hoge(huga)
    __slots__ = ["_size", "_first_idx", "_parents"]
    def __init__(self, size: int, first_index: int = 0) -> None:
        self._size = size
        self._first_idx = first_index
        self._parents = [-1] * (size + first_index)
    def find(self, x: int) -> int:
        if self._parents[x] < 0:
            return x
        self._parents[x] = self.find(self._parents[x])
        return self._parents[x]
    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    def unite(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self._parents[x] > self._parents[y]:
            x, y = y, x
        self._parents[x] += self._parents[y]
        self._parents[y] = x
        return True
    def size(self, x: int) -> int:
        return -self._parents[self.find(x)]
    def group_count(self) ->int:
        return sum(1 for i in  self._parents if i<0)-self._first_idx
    def connected(self) ->bool:
        return self._parents[self.find(self._first_idx)]==-self._size
uf=UnionFind(2*n)
for i in range(n):
    for ne in l[i]:
        uf.unite(i,ne+n)
        uf.unite(i+n,ne)

if uf.same(0,n):
    print(-1)

else:
    class WarshallFloyd:
        #O(V^3)で任意２頂点の最短距離
        def __init__(self,n,_first_index=0):
            self.v = n
            self._first_idx=_first_index
            self.d = [[float("INF")]*(n) for _ in range(n)]
            for i in range(n):
                self.d[i][i] = 0
    
        def path(self,x,y,c):
            if x == y:
                return False
            f=self._first_idx
            self.d[x-f][y-f] = c
            self.d[y-f][x-f] = c
            return True
    
        def build(self):
            for k in range(self.v):
                for i in range(self.v):
                    for j in range(self.v):
                        self.d[i][j] = min(self.d[i][j], self.d[i][k] + self.d[k][j])
            return self.d
    w=WarshallFloyd(n)
    for x in range(n):
        for j in l[x]:
            w.path(x,j,1)
    d=w.build()
    ans=0
    for i in range(n):
        ans=max(ans,max(d[i]))
    print(ans+1)
