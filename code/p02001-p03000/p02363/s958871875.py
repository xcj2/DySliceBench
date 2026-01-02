class WarshallFloyd:
    #O(V^3)で任意２頂点の最短距離
    def __init__(self,n,_first_index=0):
        self.v = n
        self._first_idx=_first_index
        self.d = [[float("INF")]*(n) for _ in range(n)]
        for i in range(n):
            self.d[i][i] = 0

    def path(self,x,y,c,directed=0):
        if x == y:
            return False
        f=self._first_idx
        self.d[x-f][y-f] = c
        if directed==0:
            self.d[y-f][x-f] = c
        return True

    def build(self):
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    self.d[i][j] = min(self.d[i][j], self.d[i][k] + self.d[k][j])
        return self.d
v,e=map(int,input().split())
w=WarshallFloyd(v)
for i in range(e):
    a,s,d=map(int,input().split())
    w.path(a,s,d,1)
d=w.build()
for i in range(v):
    if d[i][i]<0:print("NEGATIVE CYCLE");exit()
for i in d:
    for j in i[:-1]:
        print("INF"if j==float("INF") else j,end=" ")
    print(i[-1]if i[-1]!=float("INF") else "INF")
