#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return [LIST() for _ in range(n)]
def NSTR(n): return [input() for _ in range(n)]


import time


INF = float("inf")
MOD = 10**9 + 7


def bit_sum(n):
    wa = 0
    while n > 0:
        wa += n & 1
        n >>= 1
    return wa

def bit(n, k):
    return (n >> k) & 1

def main():
    start = time.time()
    N = INT()
    X = input()
    origX = X
    wa = X.count("1")
    x = 0
    px = 0
    nx = 0
    start = time.time()
    for c in X:
        x <<= 1
        px <<= 1
        nx <<= 1
        if c == "1":
            x |= 1
            px |= 1
            nx |= 1
        px %= (wa+1)
        if wa != 1:
            nx %= (wa-1)
        else:
            nx %= wa
    if wa == 1:
        nx = None
    # print(time.time()-start)
    # start = time.time()
    X = x
    table = [None]*(N+1)
    table[0] = 0
    table[1] = 1
    for i in range(1, N+1):
        table[i] = table[i % bit_sum(i)] + 1
    # print(time.time()-start)
    # start = time.time()

    for i, c in enumerate(origX):
        count = 0
        if c == "1":
            if wa == 1:
                print(0)
                continue
            x = (nx-pow(2, N-i-1, wa-1)) % (wa-1)
            print(table[x]+1)
        else:
            x = (px+pow(2, N-i-1, wa+1)) % (wa+1)
            print(table[x]+1)
    # print(time.time()-start)
    return


if __name__ == '__main__':
    main()
