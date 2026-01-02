import sys
input = sys.stdin.readline

class WeightedUnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        self.weight = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            y = self.find(self.parent[x])
            self.weight[x] += self.weight[self.parent[x]]
            self.parent[x] = y
            return y

    def union(self, x, y, w):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
            self.weight[x_root] = w - self.weight[x] + self.weight[y]
        else:
            self.parent[y_root] = x_root
            self.weight[y_root] = - w - self.weight[y] + self.weight[x]
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]


def main():
    N, M = map(int, input().split())
    wuf = WeightedUnionFind(N)
    for _ in range(M):
        l, r, d = map(int, input().split())
        if wuf.is_same(l, r):
            if wuf.diff(r, l) == d:
                continue
            else:
                print("No")
                sys.exit()
        else:
            wuf.union(r, l, d)
    print("Yes")

if __name__ == '__main__':
    main()