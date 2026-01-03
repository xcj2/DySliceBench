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
    N, x = mi()
    a = list(mi())

    cnt = max(a[0]-x, 0)
    a[0] = min(a[0], x)

    for i in range(N-1):
        if a[i]+a[i+1] > x:
            cnt += a[i]+a[i+1]-x
            if a[i+1] < a[i]+a[i+1]-x:
                a[i+1] = 0
                a[i] = x
            else:
                a[i+1] = x-a[i]
    print(cnt)


if __name__ == '__main__':
    main()