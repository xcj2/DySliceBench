import random as rng
import itertools as it
import collections as col
import heapq as hq
import sys
import copy as cp
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dump_impl(*objects):
    print(*objects, file=sys.stderr)


def dump_dummy(*objects):
    pass


dump = dump_impl if "DEBUG" in sys.argv else dump_dummy


def odd(n): return n & 1


def even(n): return not odd(n)


def comb(n, m):
    r = 1
    for i in range(1, n+1):
        r *= i
    for i in range(1, m+1):
        r //= i
    for i in range(1, n-m+1):
        r //= i
    return r


def main():
    N, P = map(int, input().split())
    A = [int(n) % 2 for n in input().split()]
    cnt0 = len([a for a in A if a == 0])
    cnt1 = len([a for a in A if a == 1])
    ans = 0
    if odd(P):
        for i in range(cnt1 + 1):
            if odd(i):
                ans += comb(cnt1, i)
    else:
        for i in range(cnt1 + 1):
            if even(i):
                ans += comb(cnt1, i)
    ans *= pow(2, cnt0)
    print(ans)


if __name__ == '__main__':
    main()
