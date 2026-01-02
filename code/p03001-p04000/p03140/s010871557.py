import bisect
import sys

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
    A = ii(str)
    B = ii(str)
    C = ii(str)
    ans = 0
    for i in range(N):
        t = A[i] != B[i]
        t += B[i] != C[i]
        t += C[i] != A[i]
        ans += max(t - 1, 0)
    return ans


if __name__ == "__main__":
    print(solve())
