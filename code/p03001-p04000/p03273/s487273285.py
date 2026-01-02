from sys import stdin


def main() -> None:
    h = next_int()
    w = next_int()
    a = [input() for _ in range(h)]

    for j in range(w - 1, -1, -1):
        flg = False
        for i in range(h):
            if a[i][j] == "#":
                flg = True

        if not flg:
            for i in range(h):
                a[i] = a[i][:j] + a[i][j + 1:]

    for i in range(h):
        if "#" in a[i]:
            print(a[i])


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