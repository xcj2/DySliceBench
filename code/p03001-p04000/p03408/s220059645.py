from sys import stdin

dic = dict()


def main() -> None:
    n = next_int()
    register(n, 1)
    m = next_int()
    register(m, -1)

    ans = 0
    for v in dic.values():
        ans = max(ans, v)

    print(ans)


def register(n: int, t: int) -> None:
    global dic
    for i in range(n):
        s = input()
        if s in dic:
            dic[s] += t
        else:
            dic[s] = t


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