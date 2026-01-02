from sys import stdin


def main() -> None:
    n, a, b = [int(next_str()) for _ in range(3)]
    ans = 0

    for i in range(1, n + 1):
        sum_of_digits_i = sum_of_digits(i)
        if a <= sum_of_digits_i <= b:
            ans += i

    print(ans)


def sum_of_digits(a: int) -> int:
    result = 0
    while a != 0:
        result += a % 10
        a //= 10
    return result


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