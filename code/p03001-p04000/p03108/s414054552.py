def main():
    """http://drken1215.hatenablog.com/entry/2019/03/03/224600
    """
    N, M=map(int, input().split())
    A, B =[],[]
    for i in  range(M):
        a,b=map(int, input().split())
        A.append(a-1)
        B.append(b-1)
        
    uf=UnionFind(N)
    cur = N * (N-1) // 2
    res =[]
    for a,b in zip(A[::-1],B[::-1]):
        res.append(cur)

        if uf.issame(a, b):
            continue
        
        sa, sb = uf.size(a),  uf.size(b)
        cur -= sa * sb
        uf.merge(a, b)

    print(*res[::-1], sep="\n")


class UnionFind:
    def __init__(self, n):
        self.par = [-1] * n
    # void init(int n) { par.assign(n, -1); }

    def root(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]
    
    def issame(self, x, y):
        return self.root(x) == self.root(y)
    
    def merge(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y: return False
        if self.par[x] > self.par[y]:
            x, y = y, x # merge technique
        self.par[x] += self.par[y]
        self.par[y] = x
        return True
    
    def size(self, x):
        return -self.par[self.root(x)]

if __name__ == "__main__":
    main()
