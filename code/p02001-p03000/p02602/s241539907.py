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

def main():
    N, K = mi()
    A = list(mi())
    for i in range(K, N):
        if A[i-K] < A[i]:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()