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

def main():
    import sys
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    union_find = UnionFind(N)
    friends = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        friends[a].append(b)
        friends[b].append(a)
        union_find.union(a, b)
    blacks = [[] for _ in range(N)]
    for _ in range(K):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        blacks[c].append(d)
        blacks[d].append(c)
    ans = []
    for i in range(N):
        a = union_find.size(i) - len(friends[i])
        for black in blacks[i]:
            if union_find.same(i, black):
                a -= 1
        ans.append(a-1)
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()