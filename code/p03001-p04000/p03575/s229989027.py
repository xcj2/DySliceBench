import sys

readline = sys.stdin.readline

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.rank = [0] * n
    
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
        
        if self.rank[x] < self.rank[y]:
            self.parents[x] = y
        else:
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

def main():
    N, M = map(int, readline().split())
    nodelist = []
    for _ in range(M):
        a, b = map(int, readline().split())
        a -= 1; b -= 1
        nodelist.append([a, b])

    ans = 0
    for i in range(M):
        uf = UnionFind(N)
        for j, node in enumerate(nodelist):
            if j == i:
                continue
            uf.union(node[0], node[1])
        parent = []
        for k in range(N):
            parent.append(uf.find(k))
        if len(set(parent)) > 1:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
