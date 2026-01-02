import math
import os
import sys
from collections import defaultdict

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 998244353

# 解説AC
N = int(sys.stdin.readline())
X = sys.stdin.readline().rstrip()
if len(X) != N:
    X = '0' * (N - len(X)) + X


def get_divisors(n):
    """
    n の約数をリストで返す
    :param int n:
    :rtype: list of int
    """
    ret = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    return ret


# @debug
def test(N, X):
    def roll(k):
        if k & 1:
            k >>= 1
        else:
            k = (k >> 1) + 2 ** (N - 1)
        return k

    X = int(X, 2)
    ret = 0
    for K in range(X + 1):
        r = 1
        k = roll(K)
        while k != K:
            k = roll(k)
            r += 1
        ret += r
        if r != N * 2 or 1:
            import numpy as np
            print(np.binary_repr(k, N), r)
    return ret


def inv_s(x):
    """
    :param str x:
    """
    return ''.join(['0' if c == '1' else '1' for c in x])


# @debug
def count(d):
    sz = N // d

    base = X[:sz] + inv_s(X[:sz])
    s = base * (N // sz)
    return int(X[:sz], 2) + (s <= X + inv_s(X))


# 全部 N * 2 で戻る
counts = defaultdict(int)
counts[N * 2] = int(X, 2) + 1

# k 回でもとに戻る
ks = [N * 2 // d for d in get_divisors(N) if d % 2 and d != 1]
for k in ks:
    d = N * 2 // k
    counts[k] = count(d)

# 数え上げ
# k の約数はカウント済みなので引く
ans_counts = defaultdict(int)
for k in sorted(ks):
    ans_counts[k] = counts[k] - sum([ans_counts[d] for d in get_divisors(k)])
ans_counts[N * 2] = counts[N * 2] - sum([ans_counts[d] for d in get_divisors(N * 2)])

ans = 0
for k, cnt in ans_counts.items():
    ans += k * cnt
    ans %= MOD
print(ans)
