# https://atcoder.jp/contests/abc117/tasks/abc117_c

import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, m = input_int_list()
    X = sorted(input_int_list())
    diffs = []
    for i in range(1, m):
        diffs.append(abs(X[i - 1] - X[i]))
    diffs = sorted(diffs)
    ans = sum(diffs[:m - n])
    if n >= m:
        print(0)
        return
    else:
        print(ans)

    return


if __name__ == "__main__":
    main()
