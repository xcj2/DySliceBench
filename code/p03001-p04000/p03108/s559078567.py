from collections import deque, Counter


class UnionFind:
    def __init__(self, v):
        self.v = v
        self._tree = list(range(v + 1))
        self._counter = Counter(self._tree)

    def _root(self, a):
        queue = deque()
        while self._tree[a] != a:
            queue.append(a)
            a = self._tree[a]
        while queue:
            index = queue.popleft()
            self._tree[index] = a
        return a

    def union(self, a, b):
        root_a = self._root(a)
        root_b = self._root(b)
        if root_a == root_b:
            return 0

        self._tree[root_b] = root_a
        ca = self._counter[root_a]
        cb = self._counter[root_b]
        self._counter[root_a] += cb
        self._counter[root_b] = 0
        return ca * cb

    def find(self, a, b):
        return self._root(a) == self._root(b)


N, M = map(int, input().split(' '))
edges = [tuple(map(int, input().split(' '))) for _ in range(M)]

dp = [0] * (M + 1)
dp[-1] = N * (N - 1) // 2
union_find = UnionFind(N)

for i in reversed(range(M)):
    if dp[i + 1] == 0:
        break
    a, b = edges[i]
    minus = union_find.union(a, b)
    dp[i] = dp[i + 1] - minus

for i in range(M):
    print(dp[i + 1])
