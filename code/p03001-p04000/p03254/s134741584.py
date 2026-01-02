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
    n, x = [next_int() for _ in range(2)]
    a = sorted([next_int() for _ in range(n)])
    ans = 0

    for i, ai in enumerate(a):
        if x < ai or (i == n - 1 and x != ai):
            break
        ans += 1
        x -= ai

    print(ans)


if __name__ == '__main__':
    main()