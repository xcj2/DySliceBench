from collections import defaultdict, deque, Counter
import sys
import heapq
import math

# input = sys.stdin.readline

sys.setrecursionlimit(1000000000)

MIN = -10 ** 9
MOD = 10 ** 9 + 7


def f(n):
    if n == 0:
        return 0, False
    a = n // 3
    b = n % 3
    if b == 0:
        return a * 2, 0
    if b == 1:
        return a * 2 + 1, 1

    return a * 2 + 1, 2


def solve(s):
    last = s[0]
    c = 1
    res = 0
    last_flag = False
    for cc in s[1:]:
        if last == cc:
            c += 1
            continue

        k, k_flag = f(c)
        if k_flag == 0:
            res += k
        elif k_flag == 1:
            res += k
            last_flag = False
        else:
            if last_flag:
                res += k + 1
                last_flag = False
            else:
                res += k
                last_flag = True
        c = 1
        last = cc
    k, k_flag = f(c)
    if k_flag == 0:
        res += k
    elif k_flag == 1:
        res += k
    else:
        if last_flag:
            res += k + 1
        else:
            res += k
    return res


def main():
    s = input()
    # N = int(input())
    print(solve(s))
    # N, A, B = [int(a) for a in input().split()]
    # A = [
    #     [int(a) for a in input().split()]
    #     for _ in range(N)
    # ]


if __name__ == '__main__':
    main()
