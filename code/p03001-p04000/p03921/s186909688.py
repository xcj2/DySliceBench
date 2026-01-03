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

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    

def main():
    N, M = map(int, input().split())
    uni = UnionFind(N + M)
    for i in range(N):
        K, *L = map(int, input().split())
        for l in L:
            uni.union(i, N + l - 1)
    
    root = set()
    for i in range(N):
        root.add(uni.find(i))
    
    if len(root) == 1:
        print('YES')
    else:
        print('NO')



main()