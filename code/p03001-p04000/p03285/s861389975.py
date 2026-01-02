from sys import stdin


def main() -> None:
    n = int(next_str())
    print(("No", "Yes")[judge(n)])


def judge(n: int) -> bool:
    price_c = 4
    price_d = 7

    for c in range(0, n // price_c + 1):
        for d in range(0, n // price_d + 1):
            if c * price_c + d * price_d == n:
                return True

    return False


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