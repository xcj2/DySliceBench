import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18

T = sys.stdin.buffer.readline().decode().rstrip()
P = sys.stdin.buffer.readline().decode().rstrip()

MASK30 = (1 << 30) - 1
MASK31 = (1 << 31) - 1
MOD = (1 << 61) - 1
MASK61 = MOD


def Mul(a, b):
    au = a >> 31
    ad = a & MASK31
    bu = b >> 31
    bd = b & MASK31
    mid = ad * bu + au * bd
    midu = mid >> 30
    midd = mid & MASK30
    return au * bu * 2 + midu + (midd << 31) + ad * bd


# mod 2^61-1を計算する関数
def CalcMod(x):
    xu = x >> 61
    xd = x & MASK61
    res = xu + xd
    if res >= MOD:
        res -= MOD
    return res


class RollingHash:
    # Verify: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B
    def __init__(self, seq, base=10 ** 9 + 7):
        """
        :param str|typing.Sequence[int] seq:
        :param int base:
        :param int mod:
        """
        if isinstance(seq, str):
            self._seq = seq = list(map(ord, seq))
        else:
            self._seq = seq

        hashes = [0] * (len(seq) + 1)
        power = [1] * (len(seq) + 1)
        for i, c in enumerate(seq):
            hashes[i + 1] = CalcMod(Mul(hashes[i], base) + c)
            power[i + 1] = CalcMod(Mul(power[i], base))
        self._hashes = hashes
        self._power = power

    def get(self, L, r):
        """
        [L, r) のハッシュ値を取得します
        :param int L:
        :param int r:
        """
        if L >= r:
            return 0
        return (self._hashes[r]  - self._hashes[L] * self._power[r - L]) % MOD


t_rh = RollingHash(T)
p_rh = RollingHash(P)

obj = p_rh.get(0, len(P))
r = len(P)
l = 0
while r <= len(T):
    if t_rh.get(l, r) == obj:
        print(l)
    r += 1
    l += 1


# S = 'ababa'
# rh = RollingHash(S)
# for l in range(len(S)):
#     for r in range(l + 1, len(S) + 1):
#         print(S[l:r], l, r, rh.get(l, r))
#
# print(t_rh._hashes)

