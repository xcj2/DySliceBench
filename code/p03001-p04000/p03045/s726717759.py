import sys
input = sys.stdin.readline

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]


def main():
    N, M = map(int, input().split())
    uni = UnionFind(N)
    for _ in range(M):
        X, Y, Z = map(int, input().split())
        X -= 1
        Y -= 1
        uni.union(X,Y)

    print(len(uni.roots()))


if __name__ == "__main__":
    main()