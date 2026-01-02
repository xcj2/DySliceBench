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

def crange(m,n):
    return range(m,n+1)

def main():
    n,m = map(int, input().strip().split())
    a = [0 for _ in range(m)]
    for i in range(m):
       a[i]  = int(input().strip())
    a = set(a)
    #eprint("a ",end=": ")
    #eprint(a)
    l=[0 for _ in crange(0,n)]
    l[0]=1
    l[1]=0 if 1 in a else 1
    for i in crange(2,n):
        l[i] = 0 if i in a else l[i-2] + l[i-1]
        #eprint("l[",i,"] ",end=": ")
        #eprint(l[i])
    print(l[n]%(10**9 + 7))


    return

if __name__ == '__main__':
    main()


'''
find a_cnt such that
for given
n (1<=n<=10**5),
m (0<=m<=n-1),
when m>=1 then 列[a_i] ( 1<=i<=m<=n-1,1<= a[i]<=n-1),

let T := { (i,j) in [0...n]**2 | i + 2*j == n and } # i,j はそれぞれ「1段登る」「2段登る」コマンドﾞを使った回数

let 列 B :=[b[i] \in {1,2}] and sum(B)==n and \forall i in [0...].sum(B[0:i]) \notin





n=|T|


'''
