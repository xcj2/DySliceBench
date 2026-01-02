import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()

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
    n = int(input())
    color = [[] for _ in range(n)]
    for v, c in enumerate(map(int, input().split())):
        color[c - 1].append(v)
    E = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        E[u].append(v)
        E[v].append(u)

    # Euler tour
    start = [-1] * n
    end = [-1] * n
    count = 0
    stack = [(~0, -1), (0, -1)]
    while stack:
        v, p = stack.pop()
        if v >= 0:
            start[v] = count
            count += 1
            for nv in E[v]:
                if nv == p:
                    continue
                stack.append((~nv, v))
                stack.append((nv, v))
        else:
            end[~v] = count

    f = lambda x : x * (x + 1) // 2
    ans = [f(n)] * n
    tree = SegmentTree([1] * n, add, 0)
    history = []
    for c in range(n):
        for v in sorted(color[c], key = lambda x : start[x], reverse = 1):
            count = 1
            for nv in E[v]:
                if start[v] > start[nv]: # nv == p
                    continue
                s = tree.sum(start[nv], end[nv])
                ans[c] -= f(s)
                count += s
            tree.add(start[v], -count)
            history.append((start[v], count))
        ans[c] -= f(tree.sum(0, n))
        while history:
            tree.add(*history.pop())

    print(*ans, sep = '\n')
resolve()