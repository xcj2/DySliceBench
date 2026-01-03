from sys import stdin


def main() -> int:
    n = next_int()
    for i in range(n, 0, -1):
        if judge(i):
            print(i)
            break
    return 0


def judge(n: int) -> bool:
    while n % 2 == 0 and n != 0:
        n //= 2
    if n == 1:
        return True
    return False


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