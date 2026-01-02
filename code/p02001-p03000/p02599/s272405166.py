##### https://atcoder.jp/contests/abc174/submissions/15644075 を1次元化

import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.buffer.readline().rstrip()
 
class SegmentTree(object):
    def __init__(self, A, dot, unit):
        n = 1 << (len(A) - 1).bit_length()
        tree = [unit] * (2 * n)
        for i, v in enumerate(A):
            tree[i + n] = v
        for i in range(n - 1, 0, -1):
            tree[i] = dot(tree[i << 1], tree[i << 1 | 1])
        self._n = n
        self._tree = tree
        self._dot = dot
        self._unit = unit
 
    def __getitem__(self, i):
        return self._tree[i + self._n]
 
    def update(self, i, v):
        i += self._n
        self._tree[i] = v
        while i != 1:
            i >>= 1
            self._tree[i] = self._dot(self._tree[i << 1], self._tree[i << 1 | 1])
 
    def add(self, i, v):
        self.update(i, self[i] + v)
 
    def sum(self, l, r):
        l += self._n
        r += self._n
        l_val = r_val = self._unit
        while l < r:
            if l & 1:
                l_val = self._dot(l_val, self._tree[l])
                l += 1
            if r & 1:
                r -= 1
                r_val = self._dot(self._tree[r], r_val)
            l >>= 1
            r >>= 1
        return self._dot(l_val, r_val)

from operator import add
def resolve():
    n, q = map(int, input().split())
    C = list(map(lambda x : int(x) - 1, input().split()))
 
    A = [0] * n
    used = [0] * n
    for i, c in enumerate(C):
        if used[c]:
            continue
        used[c] = 1
        A[i] = 1
    tree = SegmentTree(A, add, 0)
 
    next = [-1] * n
    used = [-1] * n
    for i in range(n - 1, -1, -1):
        c = C[i]
        if used[c] != -1:
            next[i] = used[c]
        used[c] = i
 
    queries = [None] * q
    for i in range(q):
        l, r = map(int, input().split())
        queries[i] = (l - 1 << 40) + (r << 20) + i
    queries.sort(reverse = 1)
    
    m = (1 << 20) - 1
    ans = [0] * q
    for l in range(n):
        while queries and queries[-1] >> 40 == l:
            lri = queries.pop()
            l = lri >> 40
            r = (lri >> 20) & m
            i = lri & m
            ans[i] = tree.sum(l, r)
        if next[l] != -1:
            tree.add(next[l], 1)
 
    print(*ans, sep = '\n')
resolve()