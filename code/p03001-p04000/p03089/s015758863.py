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


@mt
def slv(N, B):
    
    ans = []
    while B:
        for i in range(len(B)-1, -1, -1):
            if i+1 == B[i]:
                B.pop(i)
                ans.append(i+1)
                break
        else:
            break
    
    if B:
        return [-1]
    else:
        return reversed(ans)


def main():
    N = read_int()
    B = read_int_n()
    for r in slv(N, B):
        print(r)




if __name__ == '__main__':
    main()
