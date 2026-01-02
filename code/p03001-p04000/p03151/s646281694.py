# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_c

import sys
# sys.setrecursionlimit(100000)
import heapq


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    A = input_int_list()
    B = input_int_list()
    plus = []
    minus = 0
    cnt = 0

    # a < b はすべて調整の必要あり
    # a < b の補填は それぞれの b > a のうち b-a が大きいところから貪欲に補填する
    for i in range(n):
        d = B[i] - A[i]
        if d > 0:
            minus += d
            cnt += 1
        else:
            heapq.heappush(plus, d)

    while minus > 0 and plus:
        minus -= -heapq.heappop(plus)
        cnt += 1

    if minus <= 0:
        print(cnt)
    else:
        print(-1)
    return


if __name__ == "__main__":
    main()
