# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    class UnionFind():
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
    
    N,M,K=map(int,input().split())
    ans=[-1]*N
    u=UnionFind(N)
    for _ in range(M):
        A,B=map(lambda x: int(x)-1,input().split())
        u.unite(A,B)
        ans[A]-=1
        ans[B]-=1
        
    for _ in range(K):
        C,D=map(lambda x: int(x)-1,input().split())
        if u.is_same(C,D):
            ans[C]-=1
            ans[D]-=1
    
    for i in range(N):
        ans[i]+=u.size(i)
    print(*ans)

if __name__ == '__main__':
    main()
