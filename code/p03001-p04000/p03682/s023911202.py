import sys
input = sys.stdin.readline


class UnionFind():
    def __init__(self, n):
        self.parent = [-1 for _ in range(n)]

    def size(self, x):
        return -self.parent[self.find(x)]

    def find(self, x):
        if (self.parent[x] < 0):
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if (x == y):
            return False
        if (self.size(x) < self.size(y)):
            self.parent[y] += self.parent[x]
            self.parent[x] = y
        else:
            self.parent[x] += self.parent[y]
            self.parent[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    N = int(input())
    x_list = []
    y_list = []
    x_app = x_list.append
    y_app = y_list.append
    for i in range(N):
        x, y = (int(x) for x in input().split())
        x_app([x, i])
        y_app([y, i])

    x_list.sort()
    y_list.sort()
    adj = []
    adj_app = adj.append
    for i in range(N-1):
        adj_app((x_list[i + 1][0] - x_list[i][0], x_list[i + 1][1], x_list[i][1]))
        adj_app((y_list[i + 1][0] - y_list[i][0], y_list[i + 1][1], y_list[i][1]))

    adj.sort(key=lambda x: x[0])
    uf = UnionFind(N)
    ans = 0
    for edge in adj:
        if not uf.same(edge[1], edge[2]):
            ans += edge[0]
            uf.unite(edge[1], edge[2])
    print(ans)


if __name__ == '__main__':
    main()
