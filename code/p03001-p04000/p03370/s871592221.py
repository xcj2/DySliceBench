from sys import stdin


def main() -> None:
    n = next_int()
    x = next_int()

    min_m = 10 ** 9
    ans = 0

    for i in range(n):
        m = next_int()
        x -= m
        min_m = min(min_m, m)
        ans += 1

    ans += x // min_m
    print(ans)


def next_int() -> int:
    return int(next_str())


def next_str() -> str:
    result = ""
    while True:
        tmp = stdin.read(1)
        if tmp.strip() != "":
            result += tmp
        elif tmp != '\r':
            break
    return result


if __name__ == '__main__':
    main()