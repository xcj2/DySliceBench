import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    S = [list(input().rstrip()) for _ in range(N)]

    uf = UnionFindTree(N*2)
    for i in range(N):
        for j in range(i+1,N):
            if S[i][j] == '1':
                uf.union(i, j+N)
                uf.union(i+N, j)
    
    for i in range(N):
        if uf.same(i, i+N):
            print(-1)
            exit()

    D = [[10**9] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j: D[i][j] = 0
            elif S[i][j] == '1': D[i][j] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    d_max = max(max(s) for s in D)
    print(d_max+1)

class UnionFindTree:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, x):
        p = self.parent
        while p[x] >= 0: x, p[x] = p[x], p[p[x]]
        return x

    def union(self, x, y):
        x, y, p = self.find(x), self.find(y), self.parent
        if x == y: return
        if p[x] > p[y]: x, y = y, x
        p[x], p[y] = p[x] + p[y], x

    def same(self, x, y): return self.find(x) == self.find(y)
    def size(self, x): return -self.parent[self.find(x)]

if __name__ == '__main__':
    main()