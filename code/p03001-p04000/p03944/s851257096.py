from sys import stdin


def main():
    w = next_int()
    h = next_int()
    n = next_int()

    x = 0
    y = 0

    for i in range(n):
        xi, yi, a = map(int, input().split())
        if a == 1:
            x = max(x, xi)
        if a == 2:
            w = min(w, xi)
        if a == 3:
            y = max(y, yi)
        if a == 4:
            h = min(h, yi)

    print(max(0, (w - x)) * max(0, (h - y)))


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