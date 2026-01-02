
class UnionFind():
    def __init__(self,n):
        self.n = n
        #self.root < 0 であれば根で、かつ絶対値が要素数。
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def findroot(self,x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.findroot(self.root[x])
            return self.root[x]
    
    def unite(self,x,y):
        x = self.findroot(x)
        y = self.findroot(y)
        if x == y:
            return
        elif self.rank[x] < self.rank[y]:
            self.root[y] += self.root[x]
            self.root[x] = y
        else:
            self.root[x] += self.root[y]
            self.root[y] = x
            if self.rank[x]==self.rank[y]:
                self.rank[x] += 1
    
    def groupjudge(self,x,y):
        return self.findroot(x)==self.findroot(y)
        
    def count(self,x):
        return -self.root[self.findroot(x)]


## abc120 d

def combination(n,m):
    res = 1
    if m > n//2:
        m = n-m
    for i in range(m):
        res *= (n-i)
    for i in range(m):
        res //= (i+1)
    return res


n, m = map(int,input().split())
a = []
b = []
for i in range(m):
    c,d = map(int,input().split())
    a.append(c)
    b.append(d)
a = a[::-1]
b = b[::-1]

ref = UnionFind(n)
unrun = combination(n,2)
out = [unrun]*m

for i in range(m-1):
    if ref.groupjudge(a[i],b[i]):
        out[i+1] = out[i]
    else:
        ac = ref.count(a[i])
        bc = ref.count(b[i])
        ref.unite(a[i],b[i])
        out[i+1] = out[i] - ac*bc
        if c == n:
            break

for i in out[::-1]:
    print(i)

