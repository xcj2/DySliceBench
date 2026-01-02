from __future__ import print_function

import sys
input = sys.stdin.readline


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    return


# import math
# import string
# import fractions
# from fractions import Fraction
# from fractions import gcd

# def lcm(n,m):
#     return int(n*m/gcd(n,m))

# import re
# import array
# import copy
# import functools
# import operator

# import collections
# import itertools
# import bisect
# import heapq

# from heapq import heappush
# from heapq import heappop
# from heapq import heappushpop
# from heapq import heapify
# from heapq import heapreplace

# from queue import PriorityQueue as pq

# def reduce(p, q):
#     common = fractions.gcd(p, q)
#     return (p//common , q//common )
# # from itertools import accumulate
# # from collections import deque

# from operator import mul
# from functools import reduce

# def combinations_count(n, r):
#     r = min(r, n - r)
#     numer = reduce(mul, range(n, n - r, -1), 1)
#     denom = reduce(mul, range(1, r + 1), 1)
#     return numer // denom

# import random
# import time


def reverse_range(a, b):  # b < a ,  get [b, a)
    return range(b, a, -1)  # range(a, b+1, -1)


def main():
    n, m, x, y = map(int, input().strip().split())
    l_x = list(map(int, input().strip().split()))
    l_x.sort(reverse=True)
    l_y = list(map(int, input().strip().split()))
    l_y.sort()

    eprint("range ", end=": ")
    eprint([i for i in reverse_range(x, y)[::-1]])

    for i in reverse_range(x, y)[::-1]:
        if l_x[0] < i <= l_y[0]:
            print("No War")
            return
    print("War")
    return


if __name__ == '__main__':
    main()
