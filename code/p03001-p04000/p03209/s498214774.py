# -*- coding: utf-8 -*-
from sys import stdin

s_in = lambda: stdin.readline()[:-1]  # s = s_in()
d_in = lambda: int(stdin.readline())  # N = d_in()
ds_in = lambda: list(map(int, stdin.readline().split()))  # List = ds_in()


N, X = ds_in()


def num_burger(n):
    """ レベルnバーガーの厚さ """
    return 4 * 2**n - 3


def num_patti(n):
    """ レベルnバーガーのパティの数 """
    return 2 * 2**n - 1


def count_patti(n, x):
    if n == 0:
        if x == 1:
            return 1
        else:
            return 0
    else:
        if x == num_burger(n):
            return num_patti(n)
        elif x > num_burger(n-1) + 2:
            retval = num_patti(n-1) + 1
            retval += count_patti(n-1, x - num_burger(n-1) - 2)
            return retval
        elif 1 <= x - num_burger(n-1) <= 2:
            return num_patti(n-1) + (x - num_burger(n-1) - 1)
        else:
            return count_patti(n-1, x-1)


print(count_patti(N, X))
