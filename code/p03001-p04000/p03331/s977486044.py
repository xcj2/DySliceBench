import sys


def next_str() -> str:
    result = ""
    while True:
        tmp = sys.stdin.read(1)
        if tmp.strip() != "":
            result += tmp
        elif tmp != '\r':
            break
    return result


def next_int() -> int:
    return int(next_str())


def digits_sum(x: int) -> int:
    result = 0
    while x != 0:
        result += x % 10
        x //= 10
    return result


def main() -> None:
    n = next_int()
    ans = sys.maxsize

    for a in range(1, n):
        b = n - a
        ans = min(ans, digits_sum(a) + digits_sum(b))

    print(ans)


if __name__ == '__main__':
    main()