class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.sizes = [1] * (n+1)
        self.root = [1] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.root[x] = -1
            self.sizes[y] += self.sizes[x]
        else:
            self.par[y] = x
            self.root[y] = -1
            self.sizes[x] += self.sizes[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)
    
    def size(self, x):
        return self.sizes[find(x)]
    

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(m)]

all_comb = n*(n-1)/2

a = UnionFind(n)

ans = [all_comb]
for pair in reversed(lst):
    if a.same_check(pair[0], pair[1]):
        ans.append(ans[-1])
        pass
    else:
        ans.append(ans[-1] - a.sizes[a.find(pair[0])]*a.sizes[a.find(pair[1])])
        a.union(pair[0], pair[1])
    
for i in reversed(ans[:-1]):
    print(int(i))