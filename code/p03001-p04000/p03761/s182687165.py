# https://atcoder.jp/contests/abc058/tasks/arc071_a

import sys
# sys.setrecursionlimit(100000)
from collections import Counter


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    d = Counter(input())
    for _ in range(n - 1):
        s = Counter(input())
        for k, v in d.items():
            if k in s.keys():
                d[k] = min(s[k], v)
            else:
                d[k] = 0
    common_chr = sorted(d.items(), key=lambda x: x[0])
    ans = ""
    for s, cnt in common_chr:
        ans += s * cnt
    print(ans)
    return


if __name__ == "__main__":
    main()
