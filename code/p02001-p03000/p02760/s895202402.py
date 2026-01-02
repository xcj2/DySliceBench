from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate
import sys
import bisect
import string
import math
import time


def I(): return int(input())


def MI(): return map(int, input().split())


def S(): return input()


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YNL = {False: 'No', True: 'Yes'}
YNU = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def main():
    A = []
    B = []
    for i in range(3):
        A.append(LI())
        B.append([False] * 3)


    N = I()

    b = []
    for i in range(N):
        b.append(I())

    for t in range(N):
        for i in range(3):
            for j in range(3):
                if b[t] == A[i][j]:
                    B[i][j] = True

    for i in range(3):
        if B[i][0] is True and B[i][1] is True and B[i][2] is True:
            print('Yes')
            return

    for i in range(3):
        if B[0][i] is True and B[1][i] is True and B[2][i] is True:
            print('Yes')
            return

    if B[0][0] is True and B[1][1] is True and B[2][2] is True:
        print('Yes')
        return

    if B[0][2] is True and B[1][1] is True and B[0][2] is True:
        print('Yes')
        return

    print('No')


if __name__ == '__main__':
    main()
