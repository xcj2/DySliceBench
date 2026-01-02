

class DisjointSet:

    def __init__(self, N):
        self.parents = [i for i in range(N)]
        self.size = [1]*N

    def find_parent(self, x):
        path = []
        while self.parents[x] != x:
            x = self.parents[x]
            path.append(x)
        for p in path:
            self.parents[p] = x
        return x

    def find_size(self, x):
        return self.size[self.find_parent(x)]

    def union(self, x, y):
        root_x = self.find_parent(x)
        root_y = self.find_parent(y)
        if self.find_parent(root_x) != self.find_parent(root_y):
            self.parents[root_x] = root_y
            self.size[root_y] += self.size[root_x]


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, M, K = read_ints()
    disjoint_set = DisjointSet(N)
    suggestions = [-1]*N
    for _ in range(M):
        a, b = read_ints()
        a -= 1
        b -= 1
        disjoint_set.union(a, b)
        suggestions[a] -= 1
        suggestions[b] -= 1
    for _ in range(K):
        c, d = read_ints()
        c -= 1
        d -= 1
        if disjoint_set.find_parent(c) == disjoint_set.find_parent(d):
            suggestions[c] -= 1
            suggestions[d] -= 1
    return [disjoint_set.find_size(i)+suggestions[i] for i in range(N)]


if __name__ == '__main__':
    print(*solve())
