import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N = I()
X,Y = [],[]
for i in range(N):
    x,y = MI()
    X.append((x,i+1))
    Y.append((y,i+1))

X.sort()
Y.sort()


# Kruskal


class Kruskal():
    def __init__(self,n):
        self.e = []
        self.par = [i for i in range(n+1)]  # 親のノード番号
        self.rank = [0]*(n+1)
    def add(self,u,v,d):  # クラスカル法で考えるのは無向グラフ
        self.e.append([u,v,d])
    def find(self,x):  # xの根のノード番号
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def same_check(self,x,y):  # x,yが同じグループか否か
        return self.find(x) == self.find(y)
    def unite(self,x,y):  # x,yの属するグループの併合
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        elif self.rank[x] > self.rank[y]:
            self.par[y] = x
        else:
            self.par[y] = x
            self.rank[x] += 1
    def Kruskal(self):
        edges = sorted(self.e,key=lambda x: x[2])  # 距離でソート
        a = 0
        for e in edges:
            if not self.same_check(e[0],e[1]):
                self.unite(e[0],e[1])
                a += e[2]
        return a


K = Kruskal(N)
for j in range(N-1):
    x0,i0 = X[j]
    x1,i1 = X[j+1]
    K.add(i0,i1,x1-x0)
for j in range(N-1):
    y0,i0 = Y[j]
    y1,i1 = Y[j+1]
    K.add(i0,i1,y1-y0)

print(K.Kruskal())
