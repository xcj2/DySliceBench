from sys import stdin


def main() -> int:
    ans = "NO"
    a = next_int()
    b, c = map(int, input().split())

    x = a
    for i in range(b + 1):
        if x % b == c:
            ans = "YES"
            break
        x += a
    print(ans)
    return 0


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