import sys


def main() -> None:
    way = 0
    pre = 0
    ans = 1

    n = next_int()

    for i in range(n):
        now = next_int()
        if i == 0 or now - pre == 0:
            pass
        elif way == 0:
            way = sgn(now - pre)
        elif sgn(now - pre) != way:
            ans += 1
            way = 0

        pre = now

    print(ans)


def sgn(x: int) -> int:
    if x == 0:
        return 0
    if x > 0:
        return 1
    return -1

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
