import sys
from collections import defaultdict, Counter


class UnionFind(object):
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


def main():
    n, m, k = list(map(int, sys.stdin.readline().strip().split()))

    friends = defaultdict(set)
    blocks = defaultdict(set)

    for i in range(m):
        a, b = list(map(int, sys.stdin.readline().strip().split()))
        a -= 1
        b -= 1
        friends[a].add(b)
        friends[b].add(a)

    for i in range(k):
        c, d = list(map(int, sys.stdin.readline().strip().split()))
        c -= 1
        d -= 1
        blocks[c].add(d)
        blocks[d].add(c)

    uf = UnionFind(n)

    for f_key in friends:
        for child in friends[f_key]:
            # child_cur_group = parents[child]
            uf.union(f_key, child)

    # group_num_set = defaultdict(set)
    # for i in range(n):
    #     group = uf.find(i)
    #     group_num_set[group].add(i)

    ans = [0] * n
    for i in range(n):
        group = uf.find(i)
        size = uf.size(i) - 1
        size -= len(friends[i])
        for block in blocks[i]:
            block_group = uf.find(block)
            if block_group == group:
                size -= 1
        ans[i] = size


        # friend_cand = group_num_set[group]

        # true_friend_cand = friend_cand.difference(blocks[i]).difference(friends[i])
        # ans[i] = len(true_friend_cand) - 1

    return ans


result = main()
print(' '.join([str(num) for num in result]))
