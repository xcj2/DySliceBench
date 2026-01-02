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

from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N,M,K=map(int,readline().split())
    #UnionFind
    t=UnionFind(N)
    fb=[set() for _ in range(N)]
    for _ in range(M):
        a,b=map(int,readline().split())
        t.union(a-1,b-1)
        if b-1 not in fb[a-1]:
            fb[a-1].add(b-1)
        if a-1 not in fb[b-1]:
            fb[b-1].add(a-1)
    
    for _ in range(K):
        c,d=map(int,readline().split())
        if t.are_same(c-1,d-1):
            if d-1 not in fb[c-1]:
                fb[c-1].add(d-1)
            if c-1 not in fb[d-1]:
                fb[d-1].add(c-1)

    res=[0]*N
    for i in range(N):
        res[i]=t.element_count(i)-1-len(fb[i])

    print(*res)

if __name__=="__main__":
    main()