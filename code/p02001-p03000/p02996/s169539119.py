# https://atcoder.jp/contests/abc131/tasks/abc131_d

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
    """
    締切がはやい順に仕事を行う。
        全て完了できれば: Yes
        できなければ: No
    """
    n = input_int()
    hq = []
    for _ in range(n):
        a, b = input_int_list()
        heapq.heappush(hq, (b, a))
    t = 0
    while hq:
        b, a = heapq.heappop(hq)
        t += a
        if t > b:
            print("No")
            return
    print("Yes")
    return


if __name__ == "__main__":
    main()
