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
    n = next_int()
    a = [0] * n
    b = [0] * n
    ans = 0

    for i in range(n):
        a[i] = next_int()
        b[i] = next_int()

    for i in range(n - 1, -1, -1):
        a[i] += ans
        if a[i] % b[i] != 0:
            ans += abs(a[i] % b[i] - b[i])

    print(ans)


if __name__ == '__main__':
    main()