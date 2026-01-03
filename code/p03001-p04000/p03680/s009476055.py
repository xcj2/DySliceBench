from sys import stdin


def main() -> int:
    n = next_int()
    a = [next_int() for _ in range(n)]

    j = 1
    dic = dict()

    for i in range(n):
        dic[j] = True
        j = a[j - 1]
        if j in dic:
            break
        if j == 2:
            print(i + 1)
            return 0

    print(-1)
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