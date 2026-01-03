# https://atcoder.jp/contests/agc003/tasks/agc003_b

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
    tmp = 0
    ans = 0
    for i in range(1, n + 1):
        a = input_int()
        if a != 0:
            tmp += a
        else:
            ans += tmp // 2
            tmp = 0
    else:
        ans += tmp // 2
    print(ans)

    return


if __name__ == "__main__":
    main()
