import sys
input=sys.stdin.readline

class UnionFind:
    def __init__(self,n):
        self.par=[i for i in range(n)]
        self.rank=[0]*n
    def find(self,x):
        if self.par[x]==x:
            return x
        else:
            self.par[x]=self.find(self.par[x])
            return self.par[x]
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:
            return
        if self.rank[x]<self.rank[y]:
            self.par[x]=y
        else:
            self.par[y]=x
            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1
    def same_check(self,x,y):
        return self.find(x)==self.find(y)

def main():
    n,m,q=map(int,input().split())
    E=[]
    uf=UnionFind(n)
    for _ in range(q):
        a,b,c=map(int,input().split())
        if c:
            E.append((a,b)) 
        else:
            uf.union(a,b)
    s=set()
    for i in range(n):
        s.add(uf.find(i))
    k=len(s)
    if E and (k<=2 or m==n-1):
        print('No')
        return
    for a,b in E:
        if uf.same_check(a,b):
            print('No')
            return
    print('Yes' if m<=n+k*(k-3)//2 else 'No')

if __name__=='__main__':
    main()