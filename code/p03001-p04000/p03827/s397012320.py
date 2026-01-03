from sys import stdin


def main():
    n = next_int()
    s = next_str()

    maximum_value = 0
    cnt = 0

    for i in range(n):
        cnt += calc(s[i])
        maximum_value = max(maximum_value, cnt)

    print(maximum_value)


def calc(c: chr) -> int:
    if c == 'I':
        return 1
    if c == 'D':
        return -1
    return 0


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