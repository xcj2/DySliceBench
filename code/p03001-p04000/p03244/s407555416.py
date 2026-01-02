# https://atcoder.jp/contests/abc111/tasks/arc103_a

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
    V = input_int_list()
    cnt = n // 2
    even = Counter(V[0::2]).most_common()
    odd = Counter(V[1::2]).most_common()
    if even[0][0] != odd[0][0]:
        ans = (cnt) - even[0][1] + (cnt) - odd[0][1]
    else:
        if len(even) > 1 and len(odd) > 1:
            ans = min(cnt - even[0][1] + cnt - odd[1][1], cnt - even[1][1] + cnt - odd[0][1])
        elif len(even) == 1 and len(odd) == 1:
            ans = cnt
        elif len(even) == 1 and len(odd) > 1:
            ans = min(cnt - odd[1][1])
        elif len(odd) == 1 and len(even) > 1:
            ans = min(cnt - even[1][1])
    print(ans)

    return


if __name__ == "__main__":
    main()
