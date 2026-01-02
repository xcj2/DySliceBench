def main():
    class unionfind():
        def __init__(self,n):
            self.par = [i for i in range(n)]
            self.size = [1 for i in range(n)]
            self.rank = [0 for i in range(n)]
 
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
                if self.rank[x] < self.rank[y]:
                    self.rank[x]+=1
                self.par[y] = x
                self.size[x] +=self.size[y]
        def get_size(self,x):
            x = self.root(x)
            return self.size[x]
 
    import sys
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    n,m,k = map(int,input().split())
    uff = unionfind(n)
    fr = [0 for i in range(n)]
 
 
    for i in range(m):
        a,b = map(int,input().split())
        uff.unite(a-1,b-1)
        fr[a-1]+=1
        fr[b-1]+=1
 
 
    ans = [uff.get_size(i) -fr[i]-1 for i in range(n)]
 
    for i in range(k):
        c,d = map(int,input().split())
        if uff.same(c-1,d-1):
            ans[c-1] -=1
            ans[d-1] -=1
    print(*ans)
if __name__=="__main__":
    main()