#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    bingo_num = []

    for i in range(3):
        N = LI()
        bingo_num.append(N)

    N = II()

    for i in range(N):
        b = II()
        for row_i in range(3):
            for col_j in range(3):
                if bingo_num[row_i][col_j] == b:
                    bingo_num[row_i][col_j] = 0

    for i in range(3):
        if sum(bingo_num[i]) == 0:
            print("Yes")
            exit()

    for j in range(3):
        if bingo_num[0][j] + bingo_num[1][j] + bingo_num[2][j] == 0:
            print("Yes")
            exit()

    sum_naname = 0
    sum_naname_2 = 0
    for i in range(3):
        sum_naname += bingo_num[i][i]
        sum_naname_2 += bingo_num[i][2 - i]

    if sum_naname == 0 or sum_naname_2 == 0:
        print("Yes")
        exit()
    print("No")


main()
