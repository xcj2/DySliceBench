import bisect
import sys
input = sys.stdin.buffer.readline


class BIT():
    """区間加算、一点取得クエリをそれぞれO(logN)で答える"""
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def _add(self, i, val):
        while i > 0:
            self.bit[i] += val
            i -= i & -i

    def get_val(self, i):
        """i番目の値を求める"""
        i = i + 1
        s = 0
        while i <= self.n:
            s += self.bit[i]
            i += i & -i
        return s

    def add(self, l, r, val):
        """区間[l, r)にvalを加える"""
        self._add(r, val)
        self._add(l, -val)


def compress(array):
    """座標圧縮したリストを返す"""
    array2 = sorted(set(array))
    memo = {value: index for index, value in enumerate(array2)}
    return memo

n, d, a = map(int, input().split())
info = [list(map(int, input().split())) for i in range(n)]

info = sorted(info)
b = [info[i][0] for i in range(n)]
memo = compress([info[i][0] for i in range(n)])
bit = BIT(n)

for i in range(n):
    ind, val = info[i]
    bit.add(memo[ind], memo[ind] + 1, val)

ans = 0
for i in range(n):
    tmp = bit.get_val(i)
    if tmp <= 0:
        continue
    ans += -((-tmp) // a)
    nxt_ind = b[i] + 2 * d
    ii = bisect.bisect_right(b, nxt_ind)
    bit.add(i, ii, ((-tmp) // a) * a)
print(ans)