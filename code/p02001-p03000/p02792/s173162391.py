def main():
    N = int(input())
    print(solve(N))


def count(n, start, end):
    """n以下の数字でsで始まりeで終わる数字の個数
    732, 1, 2 -> 12, 102, 112, 122, ... , 192 = 11
    Examples:
        >>> count(732, 1, 2)
        11
        >>> count(25, 1, 1)
        2
        >>> count(25, 3, 3)
        1
        >>> count(100, 1, 2)
        1
        >>> count(102, 1, 2)
        2
    """

    if n <= 9:
        return 1 if start == end and start <= n else 0
    if n <= 99:
        one_digit = 1 if start == end else 0
        two_digit = 1 if start * 10 + end <= n else 0
        return one_digit + two_digit
    digit_length = len(str(n))
    # digit_length桁以下
    ret1 = count(10 ** (digit_length - 1) - 1, start, end)
    # digit_length桁
    min_cand = start * (10 ** (digit_length - 1)) + end
    if min_cand > n:
        return ret1
    ret2 = min((n-min_cand) // 10 + 1, 10 ** (digit_length - 2))
    return ret1 + ret2


def solve(n):
    """n以下の組で, (213, 382)のような末尾と先頭が等しい数の個数"""
    result = 0
    for i in range(1, 10):
        for j in range(i + 1, 10):
            result += 2 * count(n, i, j) * count(n, j, i)
    for i in range(1, 10):
        result += count(n, i, i) * count(n, i, i)
    return result


if __name__ == "__main__":
    main()
