from sys import stdin


def main():
    n = next_int()
    t = [next_int() for _ in range(n)]

    m = next_int()
    ans = [0] * m

    for i in range(m):
        p = next_int() - 1
        x = next_int()
        ans[i] += sum(t) - t[p] + x

    print("\n".join(map(str, ans)))


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