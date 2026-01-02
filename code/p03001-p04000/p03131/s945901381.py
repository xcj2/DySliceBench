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
    K, A, B = il()
    ka = K - (A - 1)
    ans = (ka // 2 - 1) * (B - A) + B
    if ka % 2 == 1:
        ans += 1
    return max(K + 1, ans)


if __name__ == "__main__":
    print(solve())
