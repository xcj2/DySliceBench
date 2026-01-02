class UnionFindTree:
    
    def __init__(self, n):
        if n == 0:
            raise Exception("n is more than 1")
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
        self.num = {}
        for i in range(n):
            self.num.update({i:1})
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.num[y] += self.num[x]
            del self.num[x]
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.num[x] += self.num[y]
            del self.num[y]
        
    
    def same(self, x, y):
        X = self.find(x)
        Y = self.find(y)
        return X == Y

def add_dict(d, a, b):
    d[a].append(b)
    d[b].append(a)

def Main(N, M, K, A, B, C, D):
    uft = UnionFindTree(N)
    df = {}
    db = {}
    for i in range(N):
        df.update({i:[]})
        db.update({i:[]})
    for i in range(M):
        uft.unite(A[i]-1, B[i]-1)
        add_dict(df, A[i]-1, B[i]-1)
    for i in range(K):
        add_dict(db, C[i]-1, D[i]-1)
    ans = []
    for i in range(N):
        num_b = 0
        for e in db[i]:
            if uft.same(i, e):
                num_b += 1
        a = uft.num[uft.find(i)] - len(df[i]) - num_b - 1
        ans.append(str(a))
    return ans
                    
def main():
    N, M, K = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(K):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    out = Main(N, M, K, A, B, C, D)
    print(" ".join(out))

if __name__ == '__main__':
    main()