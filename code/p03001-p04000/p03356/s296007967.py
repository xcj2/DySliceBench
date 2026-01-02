import sys
def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    P = list(map(lambda x:int(x)-1, input().split()))
    
    uf = UnionFindTree(N)
    for _ in range(M):
        x,y = map(int, input().split())
        uf.union(x-1,y-1)

    ind = [-1] * N
    for i in range(N):
        ind[P[i]] = i

    ans = 0
    for i in range(N):
        if P[i] == i: ans += 1
        elif uf.same(i, ind[i]): ans += 1
    print(ans)

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