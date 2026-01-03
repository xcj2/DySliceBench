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
    ans = 0
    for i in range(1 << len(S) - 1):
        output = ""
        for j in range(len(S)):
            output += S[j]
            if ((i >> j) & 1) == 1:
                output += "+"
        ans += eval(output)
    return ans


if __name__ == "__main__":
    print(solve())
