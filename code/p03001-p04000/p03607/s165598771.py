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
    A = imi(N)
    c = Counter(A)
    ans = 0
    for v in c.values():
        if v % 2 == 1:
            ans += 1
    return ans


if __name__ == "__main__":
    print(solve())
