from sys import stdin


def main():
    s = input()

    best = 0
    cnt = 0
    flg = False

    for v in s:
        if v == 'A':
            flg = True
        if flg:
            cnt += 1
        if flg and v == 'Z':
            best = cnt

    print(best)


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