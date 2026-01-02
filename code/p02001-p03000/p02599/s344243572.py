import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.buffer.readline().rstrip()

class SegmentTree(object):
    def __init__(self, A):
        n = 1 << (len(A) - 1).bit_length()
        tree = [0] * (2 * n)
        for i, v in enumerate(A):
            tree[i + n] = v
        for i in range(n - 1, 0, -1):
            tree[i] = tree[i << 1] + tree[i << 1 | 1]
        self._n = n
        self._tree = tree

    def __getitem__(self, i):
        return self._tree[i + self._n]

    def update(self, i, v):
        i += self._n
        self._tree[i] = v
        while i != 1:
            i >>= 1
            self._tree[i] = self._tree[i << 1] + self._tree[i << 1 | 1]

    def add(self, i, v):
        self.update(i, self[i] + v)

    def sum(self, l, r):
        l += self._n
        r += self._n
        l_val = r_val = 0
        while l < r:
            if l & 1:
                l_val = l_val + self._tree[l]
                l += 1
            if r & 1:
                r -= 1
                r_val = self._tree[r] + r_val
            l >>= 1
            r >>= 1
        return l_val + r_val


def resolve():
    n, q = map(int, input().split())
    C = list(map(lambda x : int(x) - 1, input().split()))

    A = [0] * n
    next = [-1] * n
    used = [-1] * n
    for i in range(n - 1, -1, -1):
        c = C[i]
        A[i] = 1
        if used[c] != -1:
            next[i] = used[c]
            A[used[c]] = 0
        used[c] = i

    tree = SegmentTree(A)
    queries = [[] for _ in range(n)]
    for i in range(q):
        l, r = map(int, input().split())
        queries[l - 1].append((r, i))

    ans = [0] * q
    for l in range(n):
        for r, i in queries[l]:
            ans[i] = tree.sum(l, r)
        if next[l] != -1:
            tree.add(next[l], 1)

    print(*ans, sep = '\n')
resolve()