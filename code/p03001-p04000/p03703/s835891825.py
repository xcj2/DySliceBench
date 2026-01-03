from itertools import accumulate
from collections import Counter
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
        size = self.N + 1
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


def coordinate_Compression_1D(A):
    #from collections import Counter
    B = sorted(list(set(A)))
    idx = {a: i for i, a in enumerate(B, start=1)}
    return [idx[a] for a in A]


if __name__ == "__main__":
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    Aacc = list(accumulate([0] + A))
    B = [a - K * i for i, a in enumerate(Aacc)]
    Bcmp = coordinate_Compression_1D(B)

    bit = BinaryIndexTree(N+10)
    ans = 0
    for i, b in enumerate(Bcmp):
        ans += bit.sum(b)
        bit.add(b, 1)
    print(ans)