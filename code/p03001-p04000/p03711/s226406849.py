# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    class UnionFind:
        def __init__(self,n):
            self.par=[i for i in range(n)]
            self.siz=[1]*n
            
        def root(self,x):
            while self.par[x]!=x:
                self.par[x]=self.par[self.par[x]]
                x=self.par[x]
            return x
        
        def unite(self,x,y):
            x=self.root(x)
            y=self.root(y)
            if x==y:
                return False
            if self.siz[x]<self.siz[y]:
                x,y=y,x
            self.siz[x]+=self.siz[y]
            self.par[y]=x
            return True
        
        def is_same(self,x,y):
            return self.root(x)==self.root(y)
        
        def size(self,x):
            return self.siz[self.root(x)]
    u=UnionFind(13)
    for x in [3,5,7,8,10,12]:
        u.unite(1,x)
    for x in [6,9,11]:
        u.unite(4,x)
    x,y=map(int,input().split())
    YesNo(u.is_same(x,y))

if __name__ == '__main__':
    main()
