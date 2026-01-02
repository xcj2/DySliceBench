# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0181


"""
import sys
from sys import stdin
input = stdin.readline


def Cond(m, n, mid, books):
    rem = mid
    i = 0
    while True:
        while rem >= books[i]:
            rem -= books[i]
            i += 1
            if i == n:
                break
        rem = mid
        m -= 1
        if i == n:
            break

    if m < 0:
        return False
    else:
        return True


def solve(m, n, books):
    ub = 1500000
    lb = max(books)

    min_width = float('inf')
    for i in range(30):
        mid = (ub + lb) // 2
        if Cond(m, n, mid, books):
            min_width = min(min_width, mid)
            ub = mid
        else:
            lb = mid
    return min_width


def main(args):
    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break
        books = [int(input()) for _ in range(n)]
        result = solve(m, n, books)
        print(result)


if __name__ == '__main__':
    main(sys.argv[1:])