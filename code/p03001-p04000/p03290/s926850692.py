import sys
import math

input = sys.stdin.readline


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return list(MI())


inf = float("inf")


def main():
    d, g = MI()
    pc = [LI() for _ in range(d)]

    ans = inf
    for bit in range(1 << d):
        c = 0
        score = 0
        for i in range(d):
            if bit & (1 << i):
                c += pc[i][0]
                score += pc[i][0] * 100 * (i + 1) + pc[i][1]

        if score >= g:
            ans = min(ans, c)
        else:
            for i in reversed(range(d)):
                if bit & (1 << i):
                    continue
                res = math.ceil((g - score) / (100 * (i + 1)))
                if res < pc[i][0]:
                    ans = min(ans, c + res)
                break

    print(ans)


if __name__ == "__main__":
    main()
