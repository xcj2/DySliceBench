import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
# MOD = 10 ** 9 + 7
# MOD = 998244353

MOD = 1000003

Q = int(sys.stdin.buffer.readline())
XDN = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(Q)]


def get_factorials(max, mod=None):
    """
    階乗 0!, 1!, 2!, ..., max!
    :param int max:
    :param int mod:
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
    逆元 0, 1/1, 1/2, 1/3, ..., 1/max
    :param int max:
    :param int mod:
    """
    invs = [1] * (max + 1)
    invs[0] = 0
    for x in range(2, max + 1):
        invs[x] = (-(mod // x) * invs[mod % x]) % mod
    return invs


def factorial_invs(max, mod):
    """
    階乗 0!, 1!, 2!, ..., max! の逆元
    :param int max:
    :param int mod:
    """
    ret = [1]
    r = 1
    for inv in mod_invs(max, mod)[1:]:
        r = r * inv % mod
        ret.append(r)
    return ret


factorials = get_factorials(MOD, MOD)
invs = mod_invs(MOD, MOD)
finvs = factorial_invs(MOD, MOD)


def solve(args):
    x, d, n = args
    if d == 0:
        return pow(x, n, MOD)
    num = x * invs[d] % MOD + n - 1
    if num >= MOD:
        return 0
    return pow(d, n, MOD) * factorials[num] % MOD * finvs[(x * invs[d] - 1) % MOD] % MOD


print(*map(solve, XDN), sep='\n')
