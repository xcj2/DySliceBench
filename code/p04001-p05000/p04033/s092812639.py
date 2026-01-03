from sys import stdin


def main() -> None:
    a = next_int()
    b = next_int()

    print(("Negative", "Zero", "Positive")[calc(a, b) + 1])


def calc(a: int, b: int) -> int:
    if a <= 0 <= b:
        return 0
    elif a > 0 or (b - a) % 2 != 0:
        return 1
    else:
        return -1


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