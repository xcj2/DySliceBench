from operator import mul
from functools import reduce
from collections import Counter
# from itertools import combinations as comb
# from itertools import permutations as perm
# from copy import copy
# 配列二分法アルゴリズム
# https://docs.python.jp/3/library/bisect.html
# import bisect
# 桁数指定
# print('{:.3f}'.format(X))
# from collections import defaultdict
# dic = defaultdict(lambda: ...)
# 値で辞書をソート
# sorted(dic.items(), key=lambda x:x[1])
# ヒープキュー
# https://docs.python.org/ja/3/library/heapq.html
# import heapq
# 正規表現(regular expression)のためのモジュール
# import re

import sys

sys.setrecursionlimit(2000)


def inpl():
    return list(map(int, input().split()))


# 重複組み合わせは nHr = (n + r - 1)Cn
def cmb(n, r):
    # combination
    if n < r:
        return 0
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def gcd(a, b):
    # greatest common divisor
    while b > 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    # least common multiple
    return a * b // gcd(a, b)


N = int(input())
A = inpl()
ans = 0
for i in range(N - 1):
    if A[i] == A[i + 1]:
        A[i + 1] = -1
        ans += 1

print(ans)
