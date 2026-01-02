from sys import stdin


def main() -> None:
    a, b = [int(next_str()) for _ in range(2)]
    ans = 0

    for i in range(a, b + 1):
        ans += judge(i)

    print(ans)


def judge(a: int) -> bool:
    s = str(a)
    n = len(s)

    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False

    return True


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