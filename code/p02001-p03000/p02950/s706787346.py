import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


# MOD = 998244353


def get_factorials(max, mod=None):
    """
    階乗 0!, 1!, 2!, ..., max!
    :param int max:
    :param int mod:
    :return:
    """
    ret = [1]
    n = 1
    if mod:
        for i in range(1, max + 1):
            n *= i
            n %= mod
            ret.append(n)
    else:
        for i in range(1, max + 1):
            n *= i
            ret.append(n)
    return ret


def mod_invs(max, mod):
    """
    逆元のリスト 0 から max まで
    :param int max:
    :param int mod:
    """
    invs = [1] * (max + 1)
    for x in range(2, max + 1):
        invs[x] = (-(mod // x) * invs[mod % x]) % mod
    return invs


def factorial_invs(max, mod):
    """
    階乗 0!, 1!, 2!, ..., max! の逆元
    :param int max:
    :param int mod:
    """
    ret = []
    r = 1
    for inv in mod_invs(max, mod):
        r = r * inv % mod
        ret.append(r)
    return ret


class Combination:
    def __init__(self, max, mod):
        """
        :param int max:
        :param int mod: 3 以上の素数であること
        """
        self._factorials = get_factorials(max, mod)
        self._finvs = factorial_invs(max, mod)
        self._mod = mod

    def ncr(self, n, r):
        """
        :param int n:
        :param int r:
        :rtype: int
        """
        if n < r:
            return 0
        return (
                self._factorials[n]
                * self._finvs[r]
                % self._mod
                * self._finvs[n - r]
                % self._mod
        )


P = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# A = np.array(A, dtype=int)
# vpow = np.vectorize(lambda a, b: pow(a, b, P))
# mat = []
# for i in range(P):
#     mat.append(vpow(i, np.arange(P)))
# print(np.array(mat).sum(axis=1) % P)
# print(np.array(mat).sum(axis=0) % P)
# mat = np.hstack((mat, [[a] for a in A]))
#
# print(mat)
#


# 解説AC
# f(x) = 1−(x - j)^(P - 1) は、x == j のとき1、それ以外のとき0
# A[j] == 1 である j について上記の式を足し合わせる
comb = Combination(max=P - 1, mod=P)
ncr = [comb.ncr(P - 1, i) for i in range(P)]
B = [0] * P
for j, a in enumerate(A):
    if a == 0:
        continue
    pw = 1  # pow(-j, i, P)
    for i in range(P):
        B[i] -= pw * ncr[i] % P
        B[i] %= P
        pw = (pw * -j) % P
    B[-1] += 1
    B[-1] %= P
print(*B[::-1])
