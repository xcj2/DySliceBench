#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def I(): return int(sys.stdin.readline())


def LS(): return [list(x) for x in sys.stdin.readline().split()]


def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res


def IR(n):
    return [I() for i in range(n)]


def LIR(n):
    return [LI() for i in range(n)]


def SR(n):
    return [S() for i in range(n)]


def LSR(n):
    return [LS() for i in range(n)]


sys.setrecursionlimit(1000000)
mod = 1000000007


def main():
    # write codes here
    A = LIR(3)
    N = I()
    B = IR(N)

    bingo_card = [[0, 0, 0] for i in range(3)]

    for b in B:
        for i in range(3):
            for j in range(3):
                if A[i][j] == b:
                    bingo_card[i][j] = 1

    flag = 0

    for i in range(3):
        if sum(bingo_card[i]) == 3:
            flag = 1
            break

        if bingo_card[0][i] + bingo_card[1][i] + bingo_card[2][i] == 3:
            flag = 1
            break

    if sum([bingo_card[i][i] for i in range(3)]) == 3:
        flag = 1

    if sum([bingo_card[i][2 - i] for i in range(3)]) == 3:
        flag = 1

    if flag == 1:
        print("Yes")
    else:
        print("No")

    return 0


# Main
if __name__ == "__main__":
    main()
