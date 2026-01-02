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
    n, m, q = MAP()
    abcd = ZIP(q)

    def ascending(X):
        for i in range(1, n):
            if A[i - 1] > A[i]:
                return False
        return True

    def point(A):
        tot = 0
        for a, b, c, d in abcd:
            if A[b - 1] - A[a - 1] == c:
                tot += d
        return tot

    def forward(A):
        # Mより小さい最後の桁
        k = None
        for i in reversed(range(n)):
            if A[i] < m:
                k = i
                break
        if k is not None:
            A[k] += 1
            for j in range(k + 1, n):
                A[j] = A[k]
        else:
            A[0] = INF

    # 昇順列を巡回する
    A = [1] * n
    ans = 0
    while ascending(A):         # O(N)
        # print(A)
        p = point(A)
        if ans <= p:
            ans = p
        forward(A)
    print(ans)

    return


if __name__ == '__main__':
    main()
