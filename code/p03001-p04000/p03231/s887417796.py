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
    if x < y:
        return gcd(y, x)
    elif y == 0:
        return x
    else:
        return gcd(y, x % y)


def lcm(x: int, y: int) -> int:
    return x * y // gcd(x, y)


def main() -> None:
    n, m = [next_int() for _ in range(2)]
    s, t = [next_str() for _ in range(2)]
    l = lcm(n, m)
    dic = dict()

    for i, c in enumerate(s):
        j = i * l // n
        dic[j] = c

    for i, c in enumerate(t):
        j = i * l // m
        if j in dic and dic[j] != c:
            print(-1)
            return

    print(l)


if __name__ == '__main__':
    main()