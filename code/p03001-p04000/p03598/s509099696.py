from sys import stdin


def main() -> None:
    n, k = [next_int() for _ in range(2)]
    a = b = 0
    for i in range(n):
        xi = next_int()
        if xi <= k // 2:
            a += xi
        else:
            b += k - xi
    print((a + b) * 2)


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