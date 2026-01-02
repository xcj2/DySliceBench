import sys, math
from functools import lru_cache
from collections import defaultdict
from decimal import Decimal
sys.setrecursionlimit(10**9)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def main():
    N = ii()
    for h in range(1, 3501):
        for n in range(1, 3501):
            if (4*h*n) - N*n - N*h == 0:
                continue
            w = N*h*n/((4*h*n) - N*n - N*h)
            if w.is_integer() and w > 0:
                print(h, n, int(w))
                return

if __name__ == '__main__':
    main()
