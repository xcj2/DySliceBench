import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


class UnionFind:
    def __init__(self, n):
        self.d = [-1] * n

    def find(self, x):
        if(self.d[x] < 0):
            return x
        self.d[x] = self.find(self.d[x])
        return self.d[x]

    def unite(self, x, y):
        xd = self.find(x)
        yd = self.find(y)
        if(xd == yd):
            return False
        if self.d[xd] > self.d[yd]:
            self.d[yd] += self.d[xd]
            self.d[xd] = yd
        else:
            self.d[xd] += self.d[yd]
            self.d[yd] = xd
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -1 * self.d[self.find(x)]


def main():
    n, m, k = map(int, input().split())
    uf = UnionFind(n)
    fr = [0] * n
    bl = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        fr[a] += 1
        fr[b] += 1
        uf.unite(a, b)
    for i in range(k):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        bl[c].append(d)
        bl[d].append(c)

    ans = [0]*n
    for i in range(n):
        t = uf.size(i)-1-fr[i]
        for j in range(len(bl[i])):
            if(uf.same(i, bl[i][j])):
                t -= 1
        ans[i] = t
    print(*ans)


main()
