import math
import random
import heapq
from collections import Counter, defaultdict
from decimal import Decimal, ROUND_HALF_UP, ROUND_CEILING
from functools import lru_cache, reduce
from itertools import combinations_with_replacement, product, combinations


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


def slv(S, K):
    d = set([])
    for i in range(len(S)):
        for j in range(i + 1, i + 1 + K):
            d.add(S[i:j])

    return sorted(d)[K - 1]


def main():
    S = read_str()
    K = read_int()
    # K = 3
    # S = ''.join([random.choice('abcdefghijklmnopqrstu') for _ in range(5000)])
    print(slv(S, K))


if __name__ == '__main__':
    main()
