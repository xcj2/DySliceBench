import random as rng
import itertools as it
import collections as col
import heapq as hq
import sys
import copy as cp
sys.setrecursionlimit(10**9)


def dump_impl(*objects):
    print(*objects, file=sys.stderr)


def dump_dummy(*objects):
    pass


dump = dump_impl if "DEBUG" in sys.argv else dump_dummy


def f(s, m, n):
    if(len(s) == n):
        print(s)
        return
    for i in range(m):
        # dump(i)
        f(s+chr(i+ord('a')), m if i < m-1 else (m+1), n)


n = int(input())
dump(n)
ans = set()
# for si in f('a', 2, n):
#    pass  # print(si)
f('a', 2, n)
