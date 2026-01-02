# Reference: https://note.nkmk.me/python-union-find/
class UnionFind:
    # if x is root: self.parents[x] = -(the number of the group nodes)
    # else: self.parents[x] = the parent of x
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # return the parent of x
    def find(self, x):
        history = []
        while self.parents[x] >= 0:
            history.append(x)
            x = self.parents[x]
        for node in history:
            self.parents[node] = x
        return x

    # merge the group of x and the group of y
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 0
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return 1

from sys import stdin
input = stdin.buffer.readline

def main():
    n, m = map(int, input().split())

    uf = UnionFind(n)

    ans = n - 1
    for _ in range(m):
        a, b = map(int, input().split())
        ans -= uf.union(a-1, b-1)

    print(ans)

main()
