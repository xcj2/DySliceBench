class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x):
        return -self.parents[self.find(x)]
    
    def isSame(self, x, y):
        return self.find(x) == self.find(y)

def solve():
    N, T = map(int,input().split())
    A = list(map(int,input().split()))

    uf = UnionFind(N)

    mn_idx_list = []
    mn = float('inf')
    max_diff = 0
    for i in range(N):
        mn = min(mn, A[i])
        if mn == A[i]:
            mn_idx_list.append(i)
        else:
            mn_idx_list.append(mn_idx_list[-1])

        max_diff = max(max_diff, A[i] - mn)
    
    for i in range(N):
        if A[i] - A[mn_idx_list[i]] == max_diff:
            uf.unite(i, mn_idx_list[i])
    
    parents_set = set()
    for i in range(N):
        if uf.size(i) == 1:
            continue
        parents_set.add(uf.find(i))
    
    print(len(parents_set))

if __name__ == '__main__':
    solve()
