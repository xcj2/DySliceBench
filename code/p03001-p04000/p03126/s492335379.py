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
    N, M = il()
    food = {i: 0 for i in range(1, M + 1)}
    for n in range(N):
        i = il()
        for x in i[1:]:
            food[x] += 1
    ans = 0
    for f in food:
        if food[f] == N:
            ans += 1
    return ans


if __name__ == "__main__":
    print(solve())
