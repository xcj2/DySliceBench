from sys import stdin


def main() -> int:
    n = next_int()
    m = next_int()
    dic = [0] * n

    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())

        dic[a] += 1
        dic[b] += 1

    for i in range(n):
        print(dic[i])

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