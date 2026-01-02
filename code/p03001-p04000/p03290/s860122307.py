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
    D, G = il()
    PC = iml(D)
    ans = 999999999

    for i in range(1 << D):
        count = 0
        score = 0
        for j in range(D):
            if i >> j & 1:
                score += PC[j][1]
                score += PC[j][0] * (j + 1) * 100
                count += PC[j][0]

        for j in range(D - 1, -1, -1):
            if i >> j & 1:
                continue
            if score >= G:
                break
            g = (j + 1) * 100
            gg = (G - score + g - 1) // g
            score += min(gg, PC[j][0]) * g
            count += min(gg, PC[j][0])
        ans = min(ans, count)
    return ans


if __name__ == "__main__":
    print(solve())