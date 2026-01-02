#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return [LIST() for _ in range(n)]


INF = float("inf")
MOD = 10**9 + 7


def main():
    N = INT()
    A = LIST()
    A.sort()
    M = A[-1] + 1
    table = [0] * (M)

    for i in A:
        if table[i] == 0:
            table[i] = -1
            for j in range(i + i, M, i):
                table[j] = 1
        elif table[i] == -1:
            # 重複しているということ
            table[i] = -2
    # print(table)
    cnt = 0
    for i in range(N):
        if table[A[i]] == -1:
            cnt += 1
    print(cnt)

    return


if __name__ == '__main__':
    main()
