import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def input():
    return sys.stdin.readline().rstrip()


def main():
    # [0 is True?, 1 is True?, ..., 10000 is True?]
    table = [False for _ in range(100001)]
    for i in range(1, 100001, 2):
        table[i] = is_prime(i) and is_prime((i + 1) // 2)

    cumsum = [0 for _ in range(100001)]
    for i in range(1, 100001):
        cumsum[i] = cumsum[i - 1]
        if table[i]:
            cumsum[i] += 1

    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        res = cumsum[r] - cumsum[l]
        if table[l]:
            res += 1
        print(res)


if __name__ == '__main__':
    main()
