from collections import defaultdict
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)


class BinaryIndexTree:  # 1-indexed
    def __init__(self, N):
        """
        INPUT
        N [int] -> 全部0で初期化
        N [list] -> そのまま初期化
        """
        if isinstance(N, int):
            self.N = N
            self.depth = N.bit_length()
            self.tree = [0] * (N + 1)
            self.elem = [0] * (N + 1)
        elif isinstance(N, list):
            self.N = len(N)
            self.depth = self.N.bit_length()
            self.tree = [0] + N
            self.elem = [0] + N
            self._init()
        else:
            raise "INVALID INPUT: input must be int or list"

    def _init(self):
        size = self.N
        for i in range(1, self.N):
            if i + (i & -i) > size:
                continue
            self.tree[i + (i & -i)] += self.tree[i]

    def add(self, i, x):
        self.elem[i] += x
        while i <= self.N:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def lower_bound(self, val):
        if val <= 0:
            return 0
        i = 0
        k = 1 << self.depth
        while k:
            if i + k <= self.N and self.tree[i + k] < val:
                val -= self.tree[i + k]
                i += k
            k >>= 1
        return i + 1


N, Q = map(int, input().split())
U = 5 * 10 ** 5 + 10

C = tuple(map(int, input().split()))
LR = [list() for _ in range(U)]
for i in range(Q):
    l, r = map(int, input().split())
    LR[r].append((l, i))

ans = [-1] * Q
bit = BinaryIndexTree(N + 5)
seen = defaultdict(int)
for i, c in enumerate(C, 1):
    if seen[c]:
        bit.add(seen[c], -1)
    bit.add(i, 1)
    seen[c] = i
    if LR[i]:
        R = bit.sum(i)
        for L, x in LR[i]:
            ans[x] = R - bit.sum(L - 1)


print(*ans, sep="\n")