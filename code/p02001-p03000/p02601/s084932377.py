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


def odd(n): return n & 1


def even(n): return not odd(n)


A, B, C = map(int, input().split())
K = int(input())
for i in range(K+1):
    for j in range(K+1):
        for k in range(K+1):
            if i+j+k > K:
                continue
            a = A*pow(2, i)
            b = B*pow(2, j)
            c = C*pow(2, k)
            if a < b and b < c:
                print("Yes")
                exit(0)
print("No")
