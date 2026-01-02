class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)) #親ノード
        self.size = [1]*n #グループの要素数
 
    def root(self, x): #root(x): xの根ノードを返す．
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x 
 
    def merge(self, x, y): #merge(x,y): xのいる組とyのいる組をまとめる
        x, y = self.root(x), self.root(y)
        if x == y: return False
        if self.size[x] < self.size[y]: x,y=y,x #xの要素数が大きいように
        self.size[x] += self.size[y] #xの要素数を更新
        self.parent[y] = x #yをxにつなぐ
        return True
 
    def issame(self, x, y): #same(x,y): xとyが同じ組ならTrue
        return self.root(x) == self.root(y)
        
    def getsize(self,x): #size(x): xのいるグループの要素数を返す
        return self.size[self.root(x)]

# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n,m = map(int, readline().split())
yoko = [list(map(int, readline().split())) for _ in range(n)]
tate = [list(map(int, readline().split())) for _ in range(m)]

INF = 10**9+5
xcoord = [-INF,0,INF]
ycoord = [-INF,0,INF]

for a,b,c in yoko: # (a,c) to (b,c)
    xcoord.append(a)
    xcoord.append(b)
    ycoord.append(c)
for d,e,f in tate: # (d,e) to (d,f)
    ycoord.append(e)
    ycoord.append(f)
    xcoord.append(d)

xcoord = list(sorted(set(xcoord)))
ycoord = list(sorted(set(ycoord)))

zaatu_x = {a:i for i,a in enumerate(xcoord)}
zaatu_y = {a:i for i,a in enumerate(ycoord)}

P = len(xcoord)
Q = len(ycoord)
QQ=Q-1


# (i,j) から右 or 上 に行けるか？
ok_up = [[0]*P for _ in range(Q)]
ok_ri = [[0]*Q for _ in range(P)]

for a,b,c in yoko: # (a,c) to (b,c)
    xa = zaatu_x[a]
    xb = zaatu_x[b]
    yc = zaatu_y[c]
    ok_up[yc-1][xa] += 1
    ok_up[yc-1][xb] -= 1


for d,e,f in tate: # (d,e) to (d,f)
    ye = zaatu_y[e]
    yf = zaatu_y[f]
    xd = zaatu_x[d]
    ok_ri[xd-1][ye] += 1
    ok_ri[xd-1][yf] -= 1

#print(ok_up)
#print(ok_ri)
"""
from itertools import accumulate
for i in range(Q):
    ok_up[i] = list(accumulate(ok_up[i]))
for j in range(P):
    ok_ri[j] = list(accumulate(ok_ri[j]))
"""
for i in range(Q):
    for j in range(P-1):
        ok_up[i][j+1] += ok_up[i][j]

for j in range(P):
    for i in range(Q-1):
        ok_ri[j][i+1] += ok_ri[j][i]

#print(*[i for i in ok_ri],sep="\n")

UF = UnionFind((P-1)*QQ)
for i in range(P-1):
    for j in range(Q-2):
        v = i*QQ+j
        if ok_up[j][i]==0: UF.merge(v,v+1)
for i in range(P-2):
    for j in range(Q-1):
        v = i*QQ+j
        if ok_ri[i][j]==0: UF.merge(v,v+QQ)
        
x0 = zaatu_x[0]
y0 = zaatu_y[0]

#print([UF.root(i) for i in range((P-1)*(Q-1))])
r = UF.root(x0*QQ+y0) 
if UF.root(0) == r:
    print("INF")
else:
    ans = 0
    for i in range(P-1):
        for j in range(Q-1):
            if UF.root(i*QQ+j) == r:
                ans += (xcoord[i+1]-xcoord[i])*(ycoord[j+1]-ycoord[j]) 
    print(ans)

#print(xcoord)
#print(ycoord)


