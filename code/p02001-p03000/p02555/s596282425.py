from sys import stdin
from math import factorial


def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))


def combinations_with_replacement_count(n, r):
    return combinations_count(n + r - 1, r)


def main():
    _in = [_.rstrip() for _ in stdin.readlines()]
    S = int(_in[0])  # type:int
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    min_ = 1
    max_ = S // 3
    ans = 0
    for i in range(min_, max_ + 1):
        mod = S - i * 3
        ans += combinations_with_replacement_count(mod + 1, i - 1) % (10**9 + 7)
    ans %= (10**9 + 7)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(ans)


if __name__ == "__main__":
    main()
