import itertools
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
        return self._factorials[n] * self._finvs[r] % self._mod * self._finvs[n - r] % self._mod


def test2(X):
    ret = 0
    for xs in itertools.permutations(X[:-1]):
        print(xs)
        a = 0
        ss = list(X)
        for x in xs:
            ret += ss[ss.index(x) + 1] - x
            a += ss[ss.index(x) + 1] - x
            ss.remove(x)
            print(ss)
        print(a)
        print()
    print(ret % MOD)
    print()
    print()


N = int(sys.stdin.buffer.readline())
X = list(map(int, sys.stdin.buffer.readline().split()))

inv2 = pow(2, MOD - 2, MOD)


def div2(n):
    return n % MOD * inv2 % MOD


def diff(A):
    ret = []
    for a, b in zip(A, A[1:]):
        ret.append(b - a)
    return ret


factorials = get_factorials(N + 10, MOD)
# test2(X)
# test(np.diff(X))

st = [0]
# 何回使うか
# わからんぽん
# https://oeis.org/A000254
for i in range(N + 1):
    st.append((i + 1) * st[-1] % MOD + factorials[i])

comb = Combination(max=N + 10, mod=MOD)
ans = 0
for i, d in enumerate(diff(X)):
    ans += d * st[i + 1] % MOD * comb.ncr(N, i + 1) % MOD * factorials[N - i - 1] % MOD
    ans %= MOD
ans *= pow(N, MOD - 2, MOD)
ans %= MOD
print(ans)

# for i in range(8):
#     N = i
#     counts = [0] * (N + 1)
#     for order in itertools.permutations(range(N)):
#         used = np.zeros(N)
#         a = 0
#         for i in order:
#             if used[:i].sum() == 0:
#                 a += 1
#                 used[i] = 1
#         counts[a] += 1
#     print(N)
#     print(counts)
#     print(counts * np.arange(N + 1))
#     print((counts * np.arange(N + 1)).sum())
#     print()
