from itertools import product
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
mod = 998244353


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


def F(a, b, c, d):
    res = 0
    nums = (a, b, c, d)
    ox = tuple(pow(2, i, mod) for i in nums)
    o = tuple(i-1 for i in ox)
    res += ox[0] * o[1] * ox[2] * o[3]
    res %= mod
    res += o[0] * ox[1] * o[2] * ox[3]
    res %= mod
    res -= o[0] * o[1] * o[2] * o[3]
    res %= mod
    res += ox[0] * ox[1] * ox[2] * ox[3]
    res %= mod
    return res


N = int(input())
XY = sorted(tuple(map(int, input().split())) for _ in range(N))
_, Y = zip(*XY)
ytoi = {y: i for i, y in enumerate(sorted(set(Y)), 1)}

bit_R = BinaryIndexTree([1] * N)
bit_L = BinaryIndexTree(N)

ans = 0
for i, y in enumerate(Y, 1):
    R = N - i
    L = i - 1
    y = ytoi[y]
    bit_R.add(y, -1)

    # 点iを原点として、第1-4象限にある点の数
    c4 = bit_R.sum(y)
    c1 = R - c4
    c3 = bit_L.sum(y)
    c2 = L - c3

    ans += F(c1, c2, c3, c4)
    ans %= mod

    bit_L.add(y, 1)

print(ans)