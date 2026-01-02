"""
102 C
"""

import math

def read_input():
    n = int(input())
    alist = list(map(int, input().split()))

    return n, alist


def sum_abs(alist, b):
    return sum([abs(a - b) for a in alist])


def submit():
    n, alist = read_input()

    alist = [a - (i + 1) for i, a in enumerate(alist)]
    alist.sort()

    if n % 2 == 0:
        b_min, b_max = alist[n // 2], alist[n // 2 + 1]
        print(min(sum_abs(alist, b_min), sum_abs(alist, b_max)))
    else:
        print(sum_abs(alist, alist[n // 2]))


if __name__ == "__main__":
    submit()