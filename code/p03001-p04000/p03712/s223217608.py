from sys import stdin


def main():
    h, w = map(int, input().split())
    a = [next_str() for _ in range(h)]

    for i in range(h + 2):
        print("#", end="")
        if not 0 < i <= h:
            print("#" * w, end="")
        else:
            print(a[i - 1], end="")
        print("#")


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