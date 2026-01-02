n,k=map(int,input().split())
l=list(map(int,input().split()))
sc=0
ans=n-k+1
INF=n+1
No=2
while No<n:
    No*=2
tree=[[0,0]]*(2*No)
for i in range(No-1,No-1+n):
    tree[i]=[l[i-No+1],l[i-No+1]]
for i in range(No-2,-1,-1):
    a,b=tree[i*2+1]
    c,d=tree[i*2+2]
    tree[i]=[max(a,c),min(b,d)]
def query(l,r):
    L=l+No-1
    R=r+No-1
    s=[-INF,INF]
    while L<=R:
        if R&1:
            a,b=tree[R]
            c,d=s
            s=[max(a,c),min(b,d)]
            R-=2
        else:
            R-=1
        if L&1:
            L-=1
        else:
            a,b=tree[L]
            c,d=s
            s=[max(a,c),min(b,d)]
        L>>=1;R>>=1
    return s
class unionfind:
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)
    def find(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if(x == y):
            return 
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def count(self, x):
        return -self.root[self.find(x)]
uf=unionfind(n)
s=set()
t=1
for i in range(n-1):
    if l[i]<l[i+1]:
        t+=1
    else:
        t=1
    if t>=k:
        s.add(i-k+2)
if len(s)>1:
    a=s.pop()
    while s:
        uf.unite(a,s.pop())
for i in range(n-k):
    b,a=query(i,i+k)
    if l[i]==a and l[i+k]==b:
        uf.unite(i,i+1)
s=set()
for i in range(n-k+1):
    s.add(uf.find(i))
print(len(s))