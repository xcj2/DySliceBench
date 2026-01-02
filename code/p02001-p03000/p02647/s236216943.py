import os

import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353

N, K = list(map(int, sys.stdin.buffer.readline().split()))
A = list(map(int, sys.stdin.buffer.readline().split()))


def test(A, K):
    A = list(A)
    for _ in range(K):
        B = [0] * N
        for i in range(N):
            b = 0
            for j in range(N):
                if A[j] >= abs(j - i):
                    b += 1
            B[i] = b
        A = B
    print(*A)
    return A


def test2(A, K):
    A = list(A)
    for _ in range(K):
        B = [0] * N
        for i in range(N):
            for j in range(N):
                if A[i] >= abs(j - i):
                    B[j] += 1
        A = B
    print(*A)
    return A


def cumsum(it):
    """
    累積和
    :param collections.Iterable it:
    """
    cs = 0
    ret = []
    for v in it:
        cs += v
        ret.append(cs)
    return ret


def solve(A, K):
    prev = A
    for _ in range(K):
        imos = [0] * (N + 1)
        for i in range(N):
            imos[max(0, i - A[i])] += 1
            imos[min(N, i + A[i] + 1)] -= 1
        prev = A
        A = cumsum(imos)[:-1]
        if prev == A:
            break
    print(*A)


# test(A,K)
# test2(A,K)

# N = len(A)
# for k in range(1000):
#     test(A, k)
solve(A, K)
