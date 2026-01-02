import itertools
import os
import sys
from collections import defaultdict

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353


N, X, D = list(map(int, sys.stdin.buffer.readline().split()))
if D < 0:
    X += (N - 1) * D
    D = -D

if X == D == 0:
    print(1)
    exit()

if D == 0:
    print(N + 1)
    exit()

# 差じゃなくて高橋くんが作れる数だけ考える
# lr[k]: mod D が k になる数のどっからどこまで作れるか
ranges = defaultdict(list)
for n in range(N + 1):
    # 選ぶ数を決めると、選ぶ数の合計 mod D が決まる
    # 選ぶ数の合計を X*n + D*y とすると
    # d を使う数は最小で 0 から n-1 までの合計
    y_min = (n - 1) * n // 2
    # d を使う数は最大で N-1 + N-2 + ... + N-n == N*n - (1 から n までの合計)
    y_max = N * n - (n + 1) * n // 2
    k = X * n % D
    ranges[k].append((X * n // D + y_min, X * n // D + y_max + 1))


def compress(li, origin=0):
    """
    座圧
    :param li:
    :param int origin:
    :rtype: list of int
    """
    *ret, = map({v: i + origin for i, v in enumerate(sorted(set(li)))}.__getitem__, li)
    return ret


def cumsum(it):
    """
    累積和
    :param collections.Iterable it:
    :return:
    """
    cs = 0
    ret = []
    for v in it:
        cs += v
        ret.append(cs)
    return ret


def count(lr):
    if len(lr) == 1:
        l, r = lr[0]
        return r - l

    # mod D で分けてるから座圧できる
    flatten = list(itertools.chain.from_iterable(lr))
    ranks = compress(flatten, origin=1)
    orig = [0] * (max(ranks) + 1)
    for r, f in zip(ranks, flatten):
        orig[r] = f

    imos = [0] * (len(ranks) + 10)
    for l, r in zip(ranks[::2], ranks[1::2]):
        imos[l] += 1
        imos[r] -= 1
    cum = cumsum(imos)

    ret = 0
    for i in range(len(cum) - 1):
        if cum[i] == 0 and cum[i + 1] > 0:
            left = orig[i + 1]
        if cum[i] > 0 and cum[i + 1] == 0:
            ret += orig[i + 1] - left
    return ret


ans = 0
i = 0
for lr in ranges.values():
    ans += count(lr)
    i += 1
print(ans)
