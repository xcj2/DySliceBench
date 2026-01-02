import sys
from collections import deque
import bisect
import copy
import heapq
import itertools
import math
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    N = int(input())
    A = read_list()
    S = 0
    for a in A:
        S += a
        S %= mod

    res = (S * S) % mod 
    for a in A:
        res -= a * a
        res %= mod
    
    res *= pow(2, mod - 2, mod)
    res %= mod
    print(res)


if __name__ == "__main__":
    main()

