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
    a = next_int()
    b = next_int()
    c = next_int()

    ans = 0
    dic = []

    flg = False
    while True:
        abc = sorted([a, b, c])
        if abc in dic:
            ans = -1
        for v in abc:
            if v % 2 != 0:
                flg = True
        if flg or ans < 0:
            break
        ans += 1
        dic += [abc]
        x = b // 2 + c // 2
        y = c // 2 + a // 2
        z = a // 2 + b // 2
        a, b, c = x, y, z

    print(ans)


if __name__ == '__main__':
    main()