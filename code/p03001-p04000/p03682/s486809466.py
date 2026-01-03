import sys
input = sys.stdin.readline


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rnk = [0] * (n + 1)

    def find_root(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    def isSameGroup(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def size(self, x):
        return -self.root[self.find_root(x)]


def main():
    N = int(input())
    x_list = []
    y_list = []
    x_app = x_list.append
    y_app = y_list.append
    for i in range(N):
        x, y = map(int, input().split())
        x_app([x, i])
        y_app([y, i])

    x_list.sort()
    y_list.sort()
    adj = []
    adj_app = adj.append
    for i in range(N-1):
        adj_app([x_list[i + 1][0] - x_list[i][0], x_list[i + 1][1], x_list[i][1]])
        adj_app([y_list[i + 1][0] - y_list[i][0], y_list[i + 1][1], y_list[i][1]])

    adj.sort(key=lambda x: x[0])
    uf = UnionFind(N)
    ans = 0
    for edge in adj:
        if not uf.isSameGroup(edge[1], edge[2]):
            ans += edge[0]
            uf.unite(edge[1], edge[2])
    print(ans)


if __name__ == '__main__':
    main()
