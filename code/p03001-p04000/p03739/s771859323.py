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


N = ii()
A = il()
ans = float("inf")
for sign in (1, -1):
    sum_a = 0
    c = 0
    for i in range(N):
        sum_a += A[i]
        if sum_a * sign <= 0:
            # +1になるまで加算
            c += abs(sum_a) + 1
            # 総和は1or-1のため
            sum_a = sign
        sign *= -1
    ans = min(ans, c)
print(ans)
