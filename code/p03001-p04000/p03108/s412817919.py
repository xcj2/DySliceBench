import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input():
    return sys.stdin.readline().rstrip()

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
    
    N,M=map(int,input().split())
    Q=[]
    for _ in range(M):
        Q.append(tuple(map(lambda x:int(x)-1,input().split())))
    uf=UnionFind(N)
    l_ans=[]
    ans=N*(N-1)//2
    for _ in range(M):
        l_ans.append(ans)
        a,b=Q.pop()
        siz_a,siz_b=uf.size(a),uf.size(b)
        if uf.unite(a,b):
            ans-=siz_a*siz_b
    for _ in range(M):
        print(l_ans.pop())
        
    
    

if __name__ == '__main__':
    main()
