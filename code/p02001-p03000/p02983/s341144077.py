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

# def round_lower(n, m_modulo):
#     n % modulo
#     return


def crange(l,r):
    return range(l,r+1)


def main():
    l,r = map(int, input().strip().split())

    if l//2019 < r//2019:
        print(0)
    else:
        l=l % 2019
        r=r%2019
        ans=sys.maxsize
        for i in crange(l,r):
            for j in crange(i+1,r):
                ans=min(ans,(i*j)%2019)
        print(ans)
    return

if __name__ == '__main__':
    main()
