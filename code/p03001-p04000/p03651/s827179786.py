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


def gcd(x: int, y: int) -> int:
    while y != 0:
        x = x % y
        x, y = y, x
    return abs(x)


def main() -> None:
    n, k = [next_int() for _ in range(2)]
    g, m = [0 for _ in range(2)]

    for i in range(n):
        a = next_int()
        if i == 0:
            g = a
            m = a
        g = gcd(g, a)
        m = max(m, a)

    if k % g == 0 and k <= m:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")


if __name__ == '__main__':
    main()