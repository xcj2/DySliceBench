import sys
from collections import Counter

sys.setrecursionlimit(200000)


def input():
    return sys.stdin.readline()[:-1]


def ii(t: type = int):
    return t(input())


def il(t: type = int):
    return list(map(t, input().split()))


def imi(N: int, t: type = int):
    return [ii(t) for _ in range(N)]


def iml(N: int, t: type = int):

    return [il(t) for _ in range(N)]


def solve():
    N = ii()
    A = il()
    A_p, A_n = [0] * N, [0] * N
    for i in range(N):
        A_p[i] = A[i] + 1
        A_n[i] = A[i] - 1
    c = Counter(A + A_p + A_n)
    m = max(c.values())
    return m


if __name__ == "__main__":
    print(solve())
