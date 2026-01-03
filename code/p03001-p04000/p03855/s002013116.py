from collections import defaultdict

class Unionfindtree:
    def __init__(self,number):
        self.par = [i for i in range(number)]
        self.rank = [0]*(number)

    def find(self,x):#親を探す
        if self.par[x] ==x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self,x,y):#x,yを繋げる
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 
        if self.rank[px]<self.rank[py]:
            self.par[px]=py
        else:
            self.par[py]=px
        if self.rank[px]==self.rank[py]:
            self.rank[px] +=1
    
    def connect(self,x,y):#親が同じかみる
        return self.find(x)==self.find(y)

N,K,L = map(int,input().split())
load = Unionfindtree(N)
train = Unionfindtree(N)
for i in range(K):
    a,b = map(int,input().split())
    load.union(a-1,b-1)
for i in range(L):
    a,b = map(int,input().split())
    train.union(a-1,b-1)

ar = [(load.find(i),train.find(i)) for i in range(N)]

dd = defaultdict(int)
for s in ar:
    dd[s] += 1
ans =[]
for i in range(N):
    ans.append(dd[ar[i]])
print(' '.join(map(str, ans)))