from sys import stdin


def main() -> None:
    n = next_int()
    mx = mn = 0

    for i in range(n):
        ai = next_int()
        if i == 0:
            mx = mn = ai
        else:
            mx = max(mx, ai)
            mn = min(mn, ai)

    print(mx - mn)


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