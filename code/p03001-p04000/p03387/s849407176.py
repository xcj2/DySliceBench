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
    A, B, C = il()
    m = max([A, B, C])
    diff = [m - A, m - B, m - C]
    c = 0
    for i, d in enumerate(diff):
        div_2 = d // 2
        if div_2 > 0:
            c += d // 2
            diff[i] -= 2 * div_2
    num_of_1 = diff.count(1)
    if num_of_1 == 1:
        c += 2
    elif num_of_1 == 2:
        c += 1
    return c


if __name__ == "__main__":
    print(solve())
