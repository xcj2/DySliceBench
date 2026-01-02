from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate
import sys
import bisect
import string
import math
import time


def I(): return int(input())


def MI(): return map(int, input().split())


def S(): return input()


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YNL = {False: 'No', True: 'Yes'}
YNU = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
# sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = True
show_flg = False


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
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots()),


def main():
    N, M, K = MI()
    uf = UnionFind(N+1)
    friends = {k: set() for k in range(1, N+1)}
    blocks = {k: set() for k in range(1, N+1)}
    # graph = [[] for i in range(N+1)]

    for i in range(M):
        A, B = MI()
        friends[A].add(B)
        friends[B].add(A)
        uf.union(A, B)

    for i in range(K):
        C, D = MI()
        blocks[C].add(D)
        blocks[D].add(C)

    # print(friends)
    # print(blocks)

    # groups = {k: set(g) for k, g in uf.all_group_members().items()}
    people = [0] * (N + 1)

    for i in range(1, N+1):
        people[i] = uf.size(i)

    ans = [0] * N
    for i in range(1, N+1):
        total_count = people[i]
        parent = uf.find(i)
        for block in blocks[i]:
            block_parent = uf.find(block)
            if block_parent == parent:
                total_count -= 1
        ans[i-1] = total_count - len(friends[i]) - 1

    print(*ans)


if __name__ == '__main__':
    main()
