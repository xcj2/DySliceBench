import copy
import math
import time
import statistics
import math
import itertools
import bisect
from decimal import *


# a = get_int()
def get_int():
    return int(input())


# a = get_string()
def get_string():
    return input()


# a_list = get_int_list()
def get_int_list():
    return [int(x) for x in input().split()]


# a_list = get_string_list():
def get_string_list():
    return input().split()


# a, b = get_int_multi()
def get_int_multi():
    return map(int, input().split())


# a_list = get_string_char_list()
def get_string_char_list():
    return list(str(input()))


# print("{} {}".format(a, b))
# a_list = [0] * a
'''
while (idx < n) and ():

    idx += 1
'''


def main():
    start = time.time()

    n, k = get_int_multi()
    p = get_int_list()
    c = get_int_list()

    kaisuu = [-1] * n
    score = [0] * n
    score_max = [0] * n

    for i in range(n):
        wk = 0
        wk2 = 0
        ichi = i
        for ii in range(n):
            ichi = p[ichi] - 1
            wk += c[ichi]
            wk2 = max(wk2, wk)
            if i == ichi:
                kaisuu[i] = ii + 1
                score[i] = wk
                score_max[i] = wk2
                break

    wk = 0
    ans = - 10 ** 20
    for i in range(n):
        ichi = p[i] - 1
        wk = c[ichi]
        wk2 = c[ichi]
        idx = 0
        while idx < k - 1:
            ichi = p[ichi] - 1
            wk += c[ichi]

            wk2 = max(wk2, wk)
            idx += 1

            # ループするならメモを使って減らす
            if (k - 1 - idx > kaisuu[ichi] * 2) and kaisuu[ichi] > 0:
                roopsuu = ((k - 1 - idx) // kaisuu[ichi]) - 1
                wk += roopsuu * score[ichi]
                idx += roopsuu * kaisuu[ichi]
                wk2 = max(wk2, max(wk, score_max[ichi]))

        ans = max(ans, wk2)
    print(ans)


if __name__ == '__main__':
    main()

