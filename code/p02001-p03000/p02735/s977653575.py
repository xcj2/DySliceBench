#!/usr/bin/env python3


def main() -> None:
    H, W = rmi()
    s = []
    for h in range(H):
        line = list(map(lambda c: c == '.', list(r())))
        s.append(line)
    dp = []
    for _ in range(H):
        dp.append([H + W + 1] * W)
    dp[0][0] = 0 if s[0][0] else 1
    for h in range(1, H):
        dp[h][0] = dp[h - 1][0] + int(s[h - 1][0] != s[h][0] and not s[h][0])
    for w in range(1, W):
        dp[0][w] = dp[0][w - 1] + int(s[0][w - 1] != s[0][w] and not s[0][w])
    for h in range(1, H):
        for w in range(1, W):
            dp[h][w] = min(dp[h - 1][w] + int(s[h - 1][w] != s[h][w] and not s[h][w]),
                           dp[h][w - 1] + int(s[h][w - 1] != s[h][w] and not s[h][w]))
    print(dp[H - 1][W - 1])


def r() -> str:
    return input().strip()


def ri() -> int:
    return int(r())


def rmi(delim: str = ' ') -> tuple:
    return tuple(map(int, input().split(delim)))


def w(data) -> None:
    print(data)


def wm(*data, delim: str = ' ') -> None:
    print(delim.join(map(str, data)))


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10 ** 9)
    main()
