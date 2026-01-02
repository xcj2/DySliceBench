#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return [LIST() for _ in range(n)]


# 昇順列の巡回
def ascending(N, M):
    # 長さN, 値0からM-1まで
    A = [0] * N
    yield A
    while True:
        # Mより小さい最後の桁
        k = None
        for i in reversed(range(N)):
            if A[i] < M - 1:
                k = i
                break
        if k is not None:
            A[k] += 1
            for j in range(k + 1, N):
                A[j] = A[k]
        else:
            return
        yield A


INF = float("inf")
MOD = 10**9 + 7


def main():
    n, m, q = MAP()
    abcd = ZIP(q)

    def point(A):
        tot = 0
        for a, b, c, d in abcd:
            if A[b - 1] - A[a - 1] == c:
                tot += d
        return tot

    # 昇順列を巡回する
    ans = 0
    for a in ascending(n, m):         # O(N)
        p = point(a)
        # print(a)
        if ans <= p:
            ans = p
    print(ans)

    return


if __name__ == '__main__':
    main()
