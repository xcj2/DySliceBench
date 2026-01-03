# -*- coding: utf-8 -*-
import sys
from collections import Counter
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N,K,L=map(int,input().split())
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
    d=UnionFind(N)
    t=UnionFind(N)
    for _ in range(K):
        p,q=map(int1,input().split())
        d.unite(p,q)
    for _ in range(L):
        r,s=map(int1,input().split())
        t.unite(r,s)
    l=[]
    for i in range(N):
        l.append((d.root(i),t.root(i)))
    c=Counter(l)
    for i in range(N):
        print(c[l[i]],end=' ')

if __name__ == '__main__':
    main()
