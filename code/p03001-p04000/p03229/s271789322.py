# https://atcoder.jp/contests/tenka1-2018-beginner/tasks/tenka1_2018_c

import sys
# sys.setrecursionlimit(100000)
from collections import deque


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    A = []
    for _ in range(n):
        A.append(input_int())
    A = sorted(A)
    dq = deque(A)
    ans = 0

    # 貪欲に最も差分が大きい組み合わせを使っていく
    left = dq.popleft()
    right = dq.pop()
    ans = abs(right - left)

    while dq:
        l = dq[0]
        r = dq[-1]
        if abs(left - l) == max(abs(left - l), abs(right - l), abs(left - r), abs(right - r)):
            ans += abs(left - l)
            left = l
            dq.popleft()
        elif abs(left - r) == max(abs(left - l), abs(right - l), abs(left - r), abs(right - r)):
            ans += abs(left - r)
            left = r
            dq.pop()
        elif abs(right - l) == max(abs(left - l), abs(right - l), abs(left - r), abs(right - r)):
            ans += abs(right - l)
            right = l
            dq.popleft()
        elif abs(right - r) == max(abs(left - l), abs(right - l), abs(left - r), abs(right - r)):
            ans += abs(right - r)
            right = r
            dq.pop()

    print(ans)


if __name__ == "__main__":
    main()
