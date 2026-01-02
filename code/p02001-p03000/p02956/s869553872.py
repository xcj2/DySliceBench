import sys
from operator import itemgetter
input = sys.stdin.readline


class BIT():
    """一点加算、区間取得クエリをそれぞれO(logN)で答える
    add: i番目にvalを加える
    get_sum: 区間[l, r)の和を求める
    """
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def _sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, val):
        """i番目にvalを加える"""
        i += 1
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def get_sum(self, l, r):
        """区間[l, r)の和を求める"""
        return self._sum(r) - self._sum(l)
      

n = int(input())
info = [tuple([i] + list(map(int, input().split()))) for i in range(n)]
MOD = 998244353

ans = [[0] * n for i in range(4)]

info = sorted(info, key = itemgetter(1))
to_ind = {x[2]: ind for ind, x in enumerate(sorted(info, key = itemgetter(2)))}

bit = BIT(n)
for j in range(n):
    i, x, y = info[j]
    tmp = bit.get_sum(0, to_ind[y])
    ans[2][i]= tmp
    ans[3][i] = j - tmp
    bit.add(to_ind[y], 1)
    
bit = BIT(n)
for j in range(n)[::-1]:
    i, x, y = info[j]
    tmp = bit.get_sum(0, to_ind[y])
    ans[1][i] = tmp
    ans[0][i] = n - j - 1 - tmp
    bit.add(to_ind[y], 1)

res = 0
pow2 = [1] * (n + 10)
for i in range(n):
    pow2[i + 1] = pow2[i] * 2
    pow2[i + 1] %= MOD

ans = list(zip(*ans))
for a1, a2, b1, b2 in ans:
    res += (pow2[a1] - 1) * (pow2[b1] - 1) * (pow2[a2 + b2])
    res %= MOD
    res += (pow2[a2] - 1) * (pow2[b2] - 1) * (pow2[a1 + b1])
    res %= MOD
    res += pow2[n - 1]
    res -= (pow2[a1] - 1) * (pow2[a2] - 1) * (pow2[b1] - 1) * (pow2[b2] - 1)
    res %= MOD
print(res % MOD)