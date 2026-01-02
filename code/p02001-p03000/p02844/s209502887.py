import sys, math
from functools import lru_cache
from collections import deque
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
    N = ii()
    S = input()
    cnt = 0
    for i in range(1000):
        ptn = str(i).zfill(3)
        j = 0
        flg = 0
        while j < N:
            if S[j] == ptn[flg]:
                flg += 1
                if flg == 3:
                    cnt += 1
                    break
            j += 1
    print(cnt)


if __name__ == '__main__':
    main()