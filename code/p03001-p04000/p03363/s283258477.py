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
    s = [0]

    for i in range(n):
        a = next_int()
        s += [s[-1] + a]

    s.sort()
    ans = 0
    cnt = 0
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            cnt += 1
        else:
            cnt = 0
        ans += cnt

    print(ans)


if __name__ == '__main__':
    main()