
class UnionFind:
    def __init__(self,n):
        self.n = n
        self.p = [i for i in range(n)]
        self.rank = [0]*n

    def same(self,x,y):
        return self.root(x)==self.root(y)

    def root(self,x):
        if x!=self.p[x]:self.p[x] = self.root(self.p[x])
        return self.p[x]

    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)
        if self.rank[y]<self.rank[x]:
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[y]==self.rank[x]:
                self.rank[y]+=1

def main():
    n,q = map(int,input().split())
    UF = UnionFind(n)
    for _ in range(q):
        a,b,c = map(int,input().split())
        if a == 0:UF.unite(b,c)
        else:
            if UF.same(b,c):print(1)
            else           :print(0)


if __name__ == '__main__':
    main()


