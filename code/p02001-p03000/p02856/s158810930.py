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


def f(S, res, d, c):
    if c == 0:
        return S, res
    
    if c % 2 == 1:
        S += d
        res += 1
        if S >= 10:
            S -= 9
            res += 1
        
    t = d * 2
    res += c // 2
    if t >= 10:
        t -= 9
        res += c // 2
    return f(S, res, t, c // 2)


def main():
    M = int(input())
    S = 0
    res = -1
    for _ in range(M):
        d, c = read_values()
        S, res = f(S, res, d, c)
    
    print(res)


if __name__ == "__main__":
    main()
