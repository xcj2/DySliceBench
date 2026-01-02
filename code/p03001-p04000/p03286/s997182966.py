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

    if N == 0:
        print(0)
        return 

    res = ""
    T = 1
    t = 0
    while N != 0:
        if N % 2 == 1:
            res += "1"
            N -= 1
        else:
            res += "0"
        T *= -2
        N //= -2
        t += 1

    print(res[::-1])


if __name__ == "__main__":
    main()