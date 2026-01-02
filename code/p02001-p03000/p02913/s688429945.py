import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


# MOD = 998244353
class RollingHash:
    # Verify: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B
    def __init__(self, seq, base=10 ** 9 + 7, mod=2 ** 89 - 1):
        """
        :param str|typing.Sequence[int] seq:
        :param int base:
        :param int mod:
        """
        if isinstance(seq, str):
            self._seq = seq = list(map(ord, seq))
        else:
            self._seq = seq
        self._base = base
        self._mod = mod

        hashes = [0] * (len(seq) + 1)
        power = [1] * (len(seq) + 1)
        for i, c in enumerate(seq):
            hashes[i + 1] = (hashes[i] * base + c) % mod
            power[i + 1] = power[i] * base % mod
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
        return (self._hashes[r] - self._hashes[L] * self._power[r - L]) % self._mod


N = int(sys.stdin.buffer.readline())
S = sys.stdin.buffer.readline().decode().rstrip()
rh = RollingHash(S)


def test(size):
    l = 0
    r = size
    hist = {}
    while r <= N:
        h = rh.get(l, r)
        if h in hist:
            pl, pr = hist[h]
            if pr <= l:
                return True
        else:
            hist[h] = l, r
        l += 1
        r += 1
    return False


ok = 0
ng = N
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if test(mid):
        ok = mid
    else:
        ng = mid
print(ok)
