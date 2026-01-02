import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input()


def read_str_n():
    return list(map(str, input().split()))


# @mt
def slv(A, B, C, K):
    ans = A - B if K % 2 == 0 else B - A
    if abs(ans) > 1e+18:
        return 'Unfair'
    return ans


def main():
    A, B, C, K = read_int_n()

    print(slv(A, B, C, K))


if __name__ == '__main__':
    main()
