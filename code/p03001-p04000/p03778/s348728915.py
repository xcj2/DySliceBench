from sys import stdin


def main() -> int:
    global W
    W = next_int()
    a, b = map(int, input().split())

    if b + W < a:
        ans = diff(b + W, a)
    elif a + W < b:
        ans = diff(a + W, b)
    else:
        ans = 0

    print(ans)
    return 0


def diff(a: int, b: int) -> int:
    return abs(a - b)


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