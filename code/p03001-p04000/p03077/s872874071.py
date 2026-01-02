# https://atcoder.jp/contests/abc123/tasks/abc123_c
import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    a = input_int()
    b = input_int()
    c = input_int()
    d = input_int()
    e = input_int()
    _min = min(a, b, c, d, e)
    ans = (n // _min) - 1 + 5
    if n % _min > 0:
        ans += 1
    print(ans)

    return


if __name__ == "__main__":
    main()
