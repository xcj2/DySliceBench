# https://atcoder.jp/contests/cf17-final/tasks/cf17_final_b

import sys
# sys.setrecursionlimit(100000)
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    s = input()
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    if abs(d["a"] - d["b"]) < 2 and abs(d["b"] - d["c"]) < 2 and abs(d["c"] - d["a"]) < 2:
        print("YES")
    else:
        print("NO")
    return


if __name__ == "__main__":
    main()
