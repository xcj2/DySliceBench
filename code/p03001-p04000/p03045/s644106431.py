import sys

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.parent[x] = y

def main():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    for i in range(M):
        X, Y, Z = map(int, input().split())
        uf.union(X-1, Y-1)
    s = set()
    for i in range(N):
        s.add(uf.find(i))
    print(len(s))

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()
