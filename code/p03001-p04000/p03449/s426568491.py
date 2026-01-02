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
    A = iml(2)
    ans = 0
    for i in range(1, N + 1):
        ans = max(ans, sum(A[0][:i]) + sum(A[1][i - 1 :]))
    return ans


if __name__ == "__main__":
    print(solve())
