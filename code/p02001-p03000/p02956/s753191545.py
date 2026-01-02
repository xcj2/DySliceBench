import itertools
import os
import sys
from collections import defaultdict

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 998244353


class BinaryIndexedTree:
    # http://hos.ac/slides/20140319_bit.pdf
    def __init__(self, size):
        """
        :param int size:
        """
        self._bit = [0] * (size + 1)
        self._size = size

    def add(self, i, w):
        """
        i 番目に w を加える
        :param int i:
        :param int w:
        :return:
        """
        x = i
        while x <= self._size:
            self._bit[x] += w
            x += x & -x

    def sum(self, i):
        """
        0 番目から i 番目までの合計
        :param int i:
        :return:
        """
        ret = 0
        x = i
        while x > 0:
            ret += self._bit[x]
            x -= x & -x
        return ret

    def __len__(self):
        return self._size


def compress(li):
    """
    大小関係を保ったまま 1 以上の数値に圧縮する。
    scipy.stats.rankdata に近い感じ
    :param list li:
    :rtype: list of int
    """
    ret = [0] * len(li)
    rank = 0
    prev = None
    for a, i in sorted([(a, i) for i, a in enumerate(li)]):
        if a != prev:
            rank += 1
        ret[i] = rank
    return ret


# 解説AC
N = int(sys.stdin.readline())
XY = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def test():
    ret = 0
    counts = defaultdict(int)
    for selection in itertools.product([0, 1], repeat=N):
        if not any(selection):
            continue
        xs = set([XY[i][0] for i, s in enumerate(selection) if s])
        ys = set([XY[i][1] for i, s in enumerate(selection) if s])
        xl = min(xs)
        xr = max(xs)
        yl = min(ys)
        yr = max(ys)
        r = 0
        for x, y in XY:
            r += xl <= x <= xr and yl <= y <= yr
        ret += r
        counts[r] += 1
    return ret


XY.sort()
Y = [y for _, y in XY]
Y = compress(Y)

# LL[i]: x が X[i] より小さくて、y が Y[i] より小さい数
# LG[i]: x が X[i] より小さくて、y が Y[i] より大きい数
LL = []
LG = []
GL = []
GG = []

bit = BinaryIndexedTree(size=N)
for i, y in enumerate(Y):
    ll = bit.sum(y)
    lg = i - ll
    gl = y - ll - 1
    gg = N - y - lg
    LL.append(ll)
    LG.append(lg)
    GL.append(gl)
    GG.append(gg)
    bit.add(y, 1)

pow2 = [1] * N
p = 1
for i in range(N - 1):
    p = p * 2 % MOD
    pow2[i + 1] = p

# 点 p = (X[i], Y[i]) が何回カウントされるか
ans = 0
for ll, lg, gl, gg in zip(LL, LG, GL, GG):
    # -- p を選ぶ --
    ans += pow2[N - 1]
    # -- p を選ばない --
    # ll, gg をそれぞれ1つ以上選ぶ
    a = (pow2[ll] - 1) * (pow2[gg] - 1) % MOD * pow2[N - ll - gg - 1]
    # lg, gl をそれぞれ1つ以上選ぶ
    b = (pow2[lg] - 1) * (pow2[gl] - 1) % MOD * pow2[N - lg - gl - 1]
    # ll, gg, gl, lg をそれぞれ1つ以上選ぶ
    c = (pow2[ll] - 1) * (pow2[gg] - 1) % MOD * (pow2[lg] - 1) * (pow2[gl] - 1) % MOD
    ans += a + b - c
    ans %= MOD
print(ans)
