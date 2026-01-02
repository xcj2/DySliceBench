#!/usr/bin/env python3
import sys

sys.setrecursionlimit(300000)

class BinaryIndexedTree(object):

    def __init__(self, n):
        # index is 1-based so vals[0] never be used
        self.n = n
        self.vals = [0] * (n + 1)

    def add(self, i, v):
        while i <= self.n:
            self.vals[i] += v
            i += i & -i

    def sum(self, i):
        ret = 0
        while i > 0:
            ret += self.vals[i]
            i -= i & -i
        return ret

    def sum_range(self, l, r):
        # l and r are 1-based index and inclusive
        return self.sum(r) - self.sum(l - 1)


def solve(N, S, Q, queries):
    trees = []
    for i in range(26):
        trees.append(BinaryIndexedTree(N))

    s = []
    for i, c in enumerate(S):
        c_idx = ord(c) - ord('a')
        if 'a' <= c <= 'z':
            trees[c_idx].add(i + 1, 1)
        s.append(c)

    for q in queries:
        if q[0] == '1':
            i, c = int(q[1]), q[2]
            p = s[i - 1]
            s[i - 1] = c
            trees[ord(p) - ord('a')].add(i, -1)
            trees[ord(c) - ord('a')].add(i, 1)
        if q[0] == '2':
            l, r = int(q[1]), int(q[2])
            ret = 0
            for tree in trees:
                cnt = tree.sum_range(l, r)
                if cnt:
                    ret += 1
            print(ret)
        #pprint(get_range_sum(1, 5, bit))
        #print(s)
        #print()

    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    S = str(next(tokens))
    Q = int(next(tokens))
    q = []
    for i in range(Q):
        q.append(list(map(str, input().split())))
    solve(N, S, Q, q)

if __name__ == '__main__':
    main()
