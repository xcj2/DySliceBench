#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# pascal = [[] for _ in range(4005)]

# pascal_triangle = [
#     [0 for _ in range(1 + i)] for i in range(4005)
#     # [0 for _ in range(1 + i)] for i in range(10)
# ]

def init():
    # pascal_triangle[0][0] = 1
    # for i in range(1, len(pascal_triangle)):
    #     for j in range(len(pascal_triangle[i])):
    #         new_value = 0
    #         if j < len(pascal_triangle[i-1]):
    #             new_value += pascal_triangle[i-1][j]
    #         if 0 <= j - 1:
    #             new_value += pascal_triangle[i-1][j-1]
    #         pascal_triangle[i][j] = new_value
    pass


# x 個の玉を y グループに分ける場合の数 (1個以上の玉のグループ)
def f2(x, y):
    # return pascal_triangle[x + y - 1][y - 1]
    n = x + y - 1
    r = y - 1
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


# x 個の玉を y グループに分ける場合の数 (0個以上の玉のグループ)
def f(x, y):
    if x < y:
        return 0
    if x == 0 and y == 0:
        return 1
    if x == 0:
        return 0
    if y == 0:
        return 0
    return f2(x - y, y)


init()

# N = 5, K = 3
N, K = list(map(int, input().split()))

for i in range(1, K + 1):
    result = f(K, i) * (
        f(N - K, i - 1) +
        f(N - K, i) +
        f(N - K, i) +
        f(N - K, i + 1)
    )
    # print('0', i)
    # print('1', f(K, i))
    # print('2', f(N - K, i - 1))
    # print('3', f(N - K, i))
    # print('4', f(N - K, i + 1))
    print(result % 1000000007)
    # print("")

# for line in pascal_triangle:
#     print(line)