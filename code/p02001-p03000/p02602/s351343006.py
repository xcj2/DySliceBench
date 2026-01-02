#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return [LIST() for _ in range(n)]
def NSTR(n): return [input() for _ in range(n)]


INF = float("inf")
MOD = 10**9 + 7


def main():
    N, K = MAP()
    A = LIST()

    for i in range(K, N):
        if A[i]/A[i-K] > 1.0:
            print("Yes")
        else:
            print("No")
    return


if __name__ == '__main__':
    main()
