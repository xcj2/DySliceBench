import sys


def main() -> None:
    x, y = [int(next_str()) for _ in range(2)]

    cnt = 0
    if abs(x) < abs(y):
        cnt += x < 0
        cnt += y < 0
    elif abs(x) > abs(y):
        cnt += x > 0
        cnt += y > 0
    else:
        cnt += sign(x) != sign(y)

    print(abs(abs(x) - abs(y)) + cnt)


def sign(n: int):
    if n == 0:
        return 0
    else:
        return n / abs(n)


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