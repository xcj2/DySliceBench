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

    n = input_int()
    A = input_int_list()
    cnt = defaultdict(int)
    for a in A:
        rank = a // 400
        if rank >= 8:
            rank = 8
        cnt[rank] += 1
    ans_min = 0
    ans_max = 0
    for k, v in sorted(cnt.items(), key=lambda x: x[0]):
        if k != 8:
            ans_min += 1
            ans_max += 1
        elif k == 8:
            if ans_min == 0:
                ans_min = 1
                ans_max = v
            else:
                ans_max += v
    print(ans_min, ans_max)

    return


if __name__ == "__main__":
    main()
