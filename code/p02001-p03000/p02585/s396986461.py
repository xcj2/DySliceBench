ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
n,k = ma()
Pt = lma()
P = [p-1 for p in Pt]
C = lma()
class unionfind():
    def __init__(self,n):
        self.par = list(range(n))
        self.size = [1]*n
        self.rank = [0]*n

    def root(self,x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self,x,y):
        return self.root(x) == self.root(y)

    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)
        if x==y:return
        else:
            if self.rank[x] < self.rank[y]:
                 x,y = y,x
            if self.rank[x] == self.rank[y]:
                self.rank[x]+=1
            self.par[y] = x
            self.size[x] +=self.size[y]
    def get_size(self,x):
        x = self.root(x)
        return self.size[x]
uf = unionfind(n)
for i in range(n):
    uf.unite(i,P[i])

def score(x):#xからスタートしたスコア
    l = uf.get_size(x)
    p,r = divmod(k,l)
    tmp = [0 for i in range(l)]#一回の累積gain
    gain_cycle = 0
    tval = 0
    for i in range(l):
        nex = P[x]
        gain_cycle +=C[nex]
        tval+=C[nex]
        tmp[i] = tval
        x = nex

    ### below::return part
    ret = -10**10
    tval = 0
    if p==0:
        for i in range(r):
            ret = max(ret,tmp[i])

    elif gain_cycle>=0:
        for i in range(l):
            if i<=r-1:
                tval=tmp[i] + gain_cycle*p
            else:
                tval=tmp[i] + gain_cycle*(p-1)
            ret = max(ret,tval)
    else:
        for i in range(l):
            ret = max(tmp[i],ret)

    return ret

        #print(ret,"ret")

ans = -10**15
for i in range(n):
    ans = max(ans,score(i))
print(ans)
