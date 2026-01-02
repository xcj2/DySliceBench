from sys import stdin


def main() -> None:
    n = next_int()
    ans = 10 ** 9

    for i in range(n):
        a = next_int()
        ans = min(ans, calc(a))
    print(ans)


def calc(a: int) -> int:
    result = 0
    while a % 2 == 0:
        result += 1
        a //= 2
    return result


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