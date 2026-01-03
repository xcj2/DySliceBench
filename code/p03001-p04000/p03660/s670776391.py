import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    G = [[] for _ in range(N)]
    E = []
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        G[a].append(b)
        G[b].append(a)
        E.append((a, b))
    par = [-1] * N
    par[N - 1] = N - 1
    stk = [N - 1]
    while stk:
        v = stk.pop()
        for to in G[v]:
            if par[to] >= 0:
                continue
            par[to] = v
            stk.append(to)
    path = []
    v = 0
    while v != N - 1:
        path.append(v)
        v = par[v]
    path.append(N - 1)
    m = (len(path) - 1) // 2
    x, y = path[m], path[m + 1]
    uf = UnionFindTree(N)
    for a, b in E:
        if a == x and b == y or a == y and b == x:
            continue
        uf.union(a, b)
    print('Fennec' if uf.size(0) > uf.size(N - 1) else 'Snuke')

class UnionFindTree:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, x):
        p = self.parent
        while p[x] >= 0: x, p[x] = p[x], p[p[x]]
        return x

    def union(self, x, y):
        x, y, p = self.find(x), self.find(y), self.parent
        if x == y: return False
        if p[x] > p[y]: x, y = y, x
        p[x], p[y] = p[x] + p[y], x
        return True

    def same(self, x, y): return self.find(x) == self.find(y)
    def size(self, x): return -self.parent[self.find(x)]

if __name__ == '__main__':
    main()
