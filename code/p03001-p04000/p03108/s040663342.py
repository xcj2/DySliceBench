class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parents=[-1]*n

    def find(self,x): #根を見つける、繋ぎ直す
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    
    def unite(self,x,y): #x,yの含むグループを併合する
        x=self.find(x)
        y=self.find(y)

        if x==y:
            return
        
        if self.parents[x]>self.parents[y]:
            x,y=y,x

        self.parents[x]+=self.parents[y]
        self.parents[y]=x
        
    def same(self,x,y):
        return self.find(x)==self.find(y)
      
    def members(self,x):
        return -self.parents[self.find(x)]
   
def main():
    import sys
    input=sys.stdin.readline
    n,m=map(int,input().split())
    bridges=[tuple(map(int,input().split())) for i in range(m)]
    
    uf=UnionFind(n)
    inco=[n*(n-1)//2]
    for i in range(m-1):
        a,b=bridges[m-i-1]
        a,b=a-1,b-1
        if uf.same(a,b):
          t=inco[i]
        else:
          t=inco[i]-uf.members(a)*uf.members(b)
        if uf.members(a)==n:
          t=0
        uf.unite(a,b)
        inco.append(t)
    print(*inco[::-1],sep='\n')

if __name__=='__main__':
    main()
