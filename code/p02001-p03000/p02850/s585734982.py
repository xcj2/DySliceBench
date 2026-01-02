from operator import mul
from functools import reduce
# from collections import Counter
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

sys.setrecursionlimit(10**6)


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


def dfs(visit, a, v_b, v_color):
    visit[a] = True

    # t_list = [t for t in tmp_list[a] if t != v_b]
    # t_color = [c for c in range(ans) if v_color != c]
    # print(t_list, t_color)
    flag = True
    i = 0
    for b in tmp_list[a]:
        if b == v_b:
            continue
        # print(a, b, c)
        # color[a][c] = True
        # color[b][c] = True
        if flag is True and i >= v_color:
            flag = False
            i += 1
        c = i
        ans_c[min(a, b), max(a, b)] = c
        dfs(visit, b, a, c)
        i += 1

    return


N = int(input())
AB = [inpl() for i in range(N - 1)]

ans_c = {}
tmp_list = [[] for i in range(N + 1)]
for a, b in AB:
    tmp_list[a].append(b)
    tmp_list[b].append(a)

ans = max(len(a) for a in tmp_list)
# print(ans, "ans")
# color = [[False for j in range(ans)] for i in range(N + 1)]
visit = [False for i in range(N + 1)]
dfs(visit, 1, N + 1, ans + 1)

print(ans)
for a, b in AB:
    print(ans_c[a, b] + 1)
