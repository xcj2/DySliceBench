#!/usr/bin/env python3

import sys

DEBUG = False

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

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def solve():
    return


def read_int_list(sep = " "):
    return [int(s) for s in sys.stdin.readline().rstrip().split(sep)]

def read_int():
    return int(sys.stdin.readline())

def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return


def main():
    n, m, k = read_int_list()
    potential_friends = UnionFind(n)
    count_friends = [0] * n
    count_blocking_in_potential_friends = [0] * n

    for _ in range(0, m):
        a, b = [p - 1 for p in read_int_list()]
        potential_friends.union(a, b)
        count_friends[a] += 1
        count_friends[b] += 1
    for _ in range(0, k):
        c, d = [p - 1 for p in read_int_list()]
        if potential_friends.same(c, d):
            count_blocking_in_potential_friends[c] += 1
            count_blocking_in_potential_friends[d] += 1
    
    ans = []
    for i in range(0, n):
        ans.append(str(potential_friends.size(i) - 1 - count_friends[i] - count_blocking_in_potential_friends[i]))

    print(" ".join(ans))


if __name__ == "__main__":
    main()