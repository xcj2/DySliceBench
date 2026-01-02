class UnionFind:
    def __init__(self,n):
        self.n=n
        self.parents=[-1]*n
        self.rank=[0]*n

    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]

    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)

        if x==y:
            return 

        if self.rank[x]<self.rank[y]:
            self.parents[y]+=self.parents[x]
            self.parents[x]=y
        else:
            self.parents[x]+=self.parents[y]
            self.parents[y]=x

            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1

    def are_same(self,x,y):
        return self.find(x)==self.find(y)

    def element_count(self,x):
        x=self.find(x)
        return -self.parents[x]

    def group_count(self):
        count=0
        for e in self.parents:
            if e<0: count+=1
        return count


from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,m=map(int,readline().split())
    a=list(map(int,readline().split()))
    uf=UnionFind(n+1)
    for i in range(m):
        x,y=map(int,readline().split())
        uf.union(x,y)

    ans=0
    for i in range(n):
        if uf.are_same(a[i],i+1):
            ans+=1
    
    print(ans)

if __name__=="__main__":
    main()