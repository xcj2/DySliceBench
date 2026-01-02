# https://atcoder.jp/contests/agc034/tasks/agc034_a

import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, a, b, c, d = input_int_list()
    S = input()

    for i in range(a - 1, max(c, d) - 1):
        if S[i] == S[i + 1] == "#":
            print("No")
            quit()
    if c < d:
        print("Yes")
        quit()
    if c > d:
        for i in range(b - 2, d - 1):
            if S[i: i + 3] == "...":
                print("Yes")
                quit()
        print("No")
        quit()


if __name__ == "__main__":
    main()
