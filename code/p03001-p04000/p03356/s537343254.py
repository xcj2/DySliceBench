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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

def func(x):
    return x - 1

def main():
    N, M = map(int, input().split())
    P = list(map(func, map(int, input().split())))
    uni = UnionFind(N)
    for _ in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        uni.union(x, y)

    cnt = 0
    for i, p in enumerate(P):
        if uni.same(i,p):
            cnt += 1
    
    print(cnt)


if __name__ == "__main__":
    main()