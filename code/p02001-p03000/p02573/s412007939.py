import sys
# sys.setrecursionlimit(100000)


class UnionFind:
    def __init__(self, n: int):
        self.nodes = n
        self.parents = [-1] * n
        self.rank = [0] * n

    # retrun the root of element x
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # unite the group include element x and group include element y
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parents[y] += self.parents[x]
            self.parents[x] = y
        else:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # get size of the gourp which element x belongs
    def get_size(self, x):
        return -self.parents[self.find(x)]

    # check if element x and element y is same group
    def same(self, x, y):
        return self.find(x) == self.find(y)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, m = input_int_list()
    union = UnionFind(n + 1)
    for _ in range(m):
        a, b = input_int_list()
        union.unite(a, b)

    ans = min(union.parents) * (-1)
    print(ans)

    return


if __name__ == "__main__":
    main()
