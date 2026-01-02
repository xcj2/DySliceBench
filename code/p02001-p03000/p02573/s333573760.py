
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
        if root_x != root_y:
            self.parents[root_x] = root_y
            self.size[root_y] += self.size[root_x]

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, M = read_ints()
    disjoint_set = DisjointSet(N)
    for _ in range(M):
        a, b = read_ints()
        disjoint_set.union(a-1, b-1)
    return max(disjoint_set.size)


if __name__ == '__main__':
    print(solve())
