# https://atcoder.jp/contests/abc116/tasks/abc116_c

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
    flowers = [0] + input_int_list()
    section_min = 0
    ans = 0
    for i in range(1, n + 1):
        if flowers[i] < flowers[i - 1]:
            ans += flowers[i - 1] - section_min
            section_min = flowers[i]
    if flowers[n] > section_min:
        ans += flowers[n] - section_min
    print(ans)
    return


if __name__ == "__main__":
    main()
