import sys
def input():
    return sys.stdin.readline()[:-1]
N,K,L=map(int,input().split())
sys.setrecursionlimit(300000)
class uf:
    def __init__(self,n):
        self.n=n
        self.l=[-1]*n
    def ro(self,n):         #root
        if self.l[n]<0:
            return n
        r=self.ro(self.l[n])
        self.l[n]=r
        return r
    def me(self,a,b):       #merge
        ra=self.ro(a-1)
        rb=self.ro(b-1)
        if self.l[ra]>self.l[rb]:
            ra,rb=rb,ra
        if ra!=rb:
            self.l[ra]+=self.l[rb]
            self.l[rb]=ra
    def size(self,n):
        return -self.l[self.ro(n)]
    def sa(self,a,b):       #same
        return self.ro(a)==self.ro(b)
    def rl(self):           #roots list
        return [i for i,v in enumerate(self.l) if v<0]
    
    def len(self):          #len(roots)
        return len(self.rl())
    def ul(self):
        d={n:i for i,n in enumerate(self.rl())}
        m=[[]for i in range(self.len())]
        for i in range(self.n):
            m[d[self.ro(i)]].append(i)
        return m
    def __str__(self):
        return f"{self.ul()}"
    def __setitem__(self,i,v):
        self.l[i]=v
up=uf(N)
for i in range(K):
    up.me(*map(int,input().split()))
ur=uf(N)
for i in range(L):
    ur.me(*map(int,input().split()))
l=[0]*N
from collections import defaultdict
for i in up.ul():
    d = defaultdict(int)
    for j in i:
        d[ur.ro(j)]+=1
    for j in i:
        l[j]=d[ur.ro(j)]
print(*l)