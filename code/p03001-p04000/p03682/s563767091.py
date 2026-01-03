ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

class UnionFind:
    def __init__(self,n):
        self.n = n
        self.d = [-1] * n

    def find(self, x):
        if(self.d[x] < 0):
            return x
        self.d[x] = self.find(self.d[x])
        return self.d[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if(x == y):
            return False
        if(self.d[x] > self.d[y]):
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self,x):
        return -self.d[self.find(x)]

n = ii()

uf = UnionFind(n)
path = [] # d,s,t

xaxis = []
yaxis = []

ans = 0
cnt = 0

for i in range(n):
    x,y = mi()
    xaxis.append([x, i])
    yaxis.append([y, i])

xaxis.sort()
yaxis.sort()

for k,i in enumerate(xaxis[1:]):
    d = i[0] - xaxis[k][0] 
    s = xaxis[k][1]
    t = i[1]
    if d != 0:
        path.append([d,s,t])
    else:
        if uf.same(s, t) == False:
            uf.union(s,t)
            cnt += 1

for k,i in enumerate(yaxis[1:]):
    d = i[0] - yaxis[k][0] 
    s = yaxis[k][1]
    t = i[1]
    if d != 0:
        path.append([d,s,t])
    else:
        if uf.same(s, t) == False:
            uf.union(s,t)
            cnt += 1

path.sort()

for i in path:
    if cnt == n-1:
        break
    d = i[0]
    s = i[1]
    t = i[2]
    if uf.same(s,t) == False:
        uf.union(s,t)
        cnt += 1
        ans += d

print(ans)





