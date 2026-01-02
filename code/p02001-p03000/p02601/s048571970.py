import sys, math
from collections import defaultdict
from itertools import product
sys.setrecursionlimit(500000)
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

def f(K, A, B, C):
    if K == 0:
        return False
    return (2*A < B < C) or f(K-1, 2*A, B, C) \
        or (A < 2*B < C) or f(K-1, A, 2*B, C) \
        or (A < B < 2*C) or f(K-1, A, B, 2*C)

def main():
    A, B, C = list(mi())
    K = ii()

    print('Yes' if f(K, A, B, C) else 'No')



if __name__ == '__main__':
    main()