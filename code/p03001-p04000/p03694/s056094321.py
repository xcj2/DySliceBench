from sys import stdin
from sys import maxsize


def main() -> int:
    n = next_int()
    lowest = maxsize
    highest = 0

    for _ in range(n):
        ai = next_int()
        lowest = min(lowest, ai)
        highest = max(highest, ai)

    print(highest - lowest)
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