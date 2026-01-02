import sys


def main() -> None:
    n = next_int()
    t = next_int()
    a = next_int()

    key = 0
    val = sys.maxsize

    for i in range(n):
        h = next_int()
        p = t - h * 0.006
        if val > abs(a - p):
            key = i + 1
            val = abs(a - p)

    print(key)


def next_int() -> int:
    return int(next_str())


def next_str() -> str:
    result = ""
    while True:
        tmp = sys.stdin.read(1)
        if tmp.strip() != "":
            result += tmp
        elif tmp != '\r':
            break
    return result


if __name__ == '__main__':
    main()