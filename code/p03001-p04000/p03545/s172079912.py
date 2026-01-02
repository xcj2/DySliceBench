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
    S = ii(str)
    A, B, C, D = (s for s in S)
    for i in ("+", "-"):
        for j in ("+", "-"):
            for k in ("+", "-"):
                s = A + i + B + j + C + k + D
                if eval(s) == 7:
                    return s + "=7"


if __name__ == "__main__":
    print(solve())
