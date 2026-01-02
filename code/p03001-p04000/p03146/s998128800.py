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


def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def solve():
    s = ii()
    d = {s: 0}
    for i in range(1, 1000000000):
        s = f(s)
        if d.get(s) is None:
            d[s] = 0
        else:
            return i + 1


if __name__ == "__main__":
    print(solve())
