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


def main() -> None:
    n, p = [next_int() for _ in range(2)]
    odd = even = 0

    for i in range(n):
        a = next_int()
        odd += a % 2
        even += (a % 2) ^ 1

    if odd == 0:
        print(2 ** even * int(p == 0))
    else:
        print((2 ** (odd - 1)) * (2 ** even))


if __name__ == '__main__':
    main()