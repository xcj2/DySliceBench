# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input().strip()


def read_str_n():
    return list(map(str, input().split()))


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap


def divisor(n):
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


@mt
def slv(A, B):
    ad = [v for v in divisor(A)]
    bd = [v for v in divisor(B)]
    cd = list(set(ad) & set(bd))
    cd.sort()
    ans = [1]
    for i in range(1, len(cd)):
        for j in range(1, i):
            if cd[i] % cd[j] == 0:
                break
        else:
            ans.append(cd[i])
    
    return len(ans)




def main():
    A, B = read_int_n()
    print(slv(A, B))

    # A = random.randint(10**11, 10**12)
    # B = random.randint(10**11, 10**12)
    # print(A, B)
    # print(slv(A, B))


if __name__ == '__main__':
    main()
