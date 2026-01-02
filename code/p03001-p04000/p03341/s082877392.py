# https://atcoder.jp/contests/arc098/tasks/arc098_a

import sys
from collections import Counter
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    S = input()
    count = Counter(S)
    left_w = 0
    left_e = 0
    ans = len(S) + 1
    for i in range(len(S)):
        if S[i] == "E":
            ans = min(ans, left_w + (count["E"] - left_e - 1))
        else:
            ans = min(ans, left_w + (count["E"] - left_e))
        if S[i] == "W":
            left_w += 1
        else:
            left_e += 1
    print(ans)
    return


if __name__ == "__main__":
    main()
