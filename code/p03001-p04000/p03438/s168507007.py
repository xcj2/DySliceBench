import sys


def next_str() -> str:
    result = ""
    while True:
        next_chr = sys.stdin.read(1)
        if next_chr.strip() != "":
            result += next_chr
        elif next_chr != '\r':
            break
    return result


def next_int() -> int:
    return int(next_str())


n = next_int()
A = [next_int() for i in range(n)]
B = [next_int() for i in range(n)]

savings = 0


def main() -> None:
    global savings
    for i in range(n):
        c = B[i] - A[i]
        if c > 0:
            savings += c // 2
        else:
            savings += c

    print(["Yes", "No"][savings < 0])


if __name__ == '__main__':
    main()
