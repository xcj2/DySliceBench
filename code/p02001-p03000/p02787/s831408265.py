def main() -> None:
    H, N = rmi()
    AB = []
    for _ in range(N):
        AB.append(rmi())
    dp = [10 ** 9] * (H + 1)
    dp[0] = 0
    for damage, mp in AB:
        for i in range(len(dp)):
            prev = max(i - damage, 0)
            dp[i] = min(dp[i], dp[prev] + mp)
    w(dp[H])


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
    main()
