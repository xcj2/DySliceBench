import sys
def main():
    input = sys.stdin.readline
    N,M=map(int, input().split())
    AB=[tuple(map(lambda x:int(x)-1, input().split())) for _ in range(M)]

    uf = UnionFindTree(N)
    mx = N*(N-1)//2
    ans = [mx]*M
    for i in range(M-1,0,-1):
        a,b = AB[i]
        ans[i-1] = ans[i] - (0 if uf.same(a, b) else uf.size(a)*uf.size(b))
        uf.union(a, b)

    for a in ans: print(a)

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