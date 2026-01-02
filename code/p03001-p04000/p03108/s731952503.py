import sys
sys.setrecursionlimit(10**9)
class UnionFind:
    def __init__(self,n):
        super().__init__()
        self.par = [-1]*n
        self.rank = [0]*n
        self.tsize = [1]*n

    
    def root(self,x):
        if self.par[x] == -1:
            return x 
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x_r = self.root(x)
        y_r = self.root(y)
        
        if self.rank[x_r]>self.rank[y_r]:
            self.par[y_r] = x_r

        elif self.rank[x_r]<self.rank[y_r]:
            self.par[x_r] = y_r

        elif x_r != y_r:
            self.par[y_r] = x_r
            self.rank[x_r] += 1

        if x_r != y_r:
            size = self.tsize[x_r]+self.tsize[y_r]
            self.tsize[x_r] = size
            self.tsize[y_r] = size

    def isSame(self,x,y):
        return self.root(x) == self.root(y)

    def size(self,x):
        return self.tsize[self.root(x)]


def main():
    n,m = tuple([int(t)for t in input().split()])

    bridge = [tuple([int(t)-1 for t in input().split()])for _ in [0]*m]
    bridge = bridge[::-1]

    uf = UnionFind(n)
    ans = [n*(n-1)//2]
    for a_i,b_i in bridge:
        if not uf.isSame(a_i,b_i):
            ans.append(ans[-1]-uf.size(a_i)*uf.size(b_i))
            uf.unite(a_i,b_i)
        else:
            ans.append(ans[-1])
    ans.pop()
    for a in ans[::-1]:
        print(a)



if __name__ == "__main__":
    main()