from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, accumulate
import itertools
import heapq
import sys
import bisect
import string
import math
import time


def I(): return int(input())


def S(): return input()


def MI(): return map(int, input().split())


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat[i])


yn = {False: 'No', True: 'Yes'}
YN = {False: 'NO', True: 'YES'}
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
    N = I()
    A = LI()
    A = sorted(A)

    cur = 0
    value = 1
    if N % 2 == 1:
        cur = 1
        value = 2
        if A[0] != 0:
            print(0)
            return

    while cur < N:
        if not (A[cur] == value and A[cur+1] == value):
            print(0)
            return
        cur += 2
        value += 2

    if N % 2 == 1:
        print(pow(2, (N - 1) // 2, MOD))
    else:
        print(pow(2, N // 2, MOD))


if __name__ == '__main__':
    main()
