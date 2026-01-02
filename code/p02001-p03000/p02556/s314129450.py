import sys
from collections import deque
from functools import lru_cache
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


class V:
    def __init__(self, f, v=None):
        self.f = f
        self.v = v
 
    def __str__(self):
        return str(self.v)
 
    def ud(self, n):
        if n is None:
            return

        if self.v is None:
            self.v = n
            return
        self.v = self.f(self.v, n) 


def main():
    N = int(input())
    P = [tuple(read_values()) for _ in range(N)]
    mX = V(min)
    MX = V(max)
    mY = V(min)
    MY = V(max)

    for p in P:
        x = p[0] + p[1]
        y = p[0] - p[1]
        mX.ud(x)
        MX.ud(x)
        mY.ud(y)
        MY.ud(y)
    
    print(max(MX.v - mX.v, MY.v - mY.v))


if __name__ == "__main__":
    main()

