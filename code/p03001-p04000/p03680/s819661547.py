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
    A = [0]+imi(N)
    current = 1
    for i in range(1, 100001):
        current = A[current]
        if current == 2:
            return i
    return -1


if __name__ == "__main__":
    print(solve())
