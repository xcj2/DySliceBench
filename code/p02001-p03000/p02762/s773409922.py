import sys
# sys.setrecursionlimit(100000)
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


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


def main():
    n, m, k = input_int_list()
    union = UnionFind(n + 1)
    friends = defaultdict(set)
    blocks = defaultdict(set)

    for i in range(m):
        a, b = input_int_list()
        friends[a].add(b)
        friends[b].add(a)
        union.unite(a, b)

    for j in range(k):
        a, b = input_int_list()
        # 同一グループでブロックしている人のみ記録する。
        if union.same(a, b):
            blocks[a].add(b)
            blocks[b].add(a)
    ans = []
    for i in range(1, n + 1):
        ans.append(union.get_size(i) - len(friends[i]) - len(blocks[i]) - 1)

    print(*ans)
    return


if __name__ == "__main__":
    main()
