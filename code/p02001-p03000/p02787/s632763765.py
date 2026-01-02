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


YN = {False: 'No', True: 'Yes'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


show_flg = True
show_flg = False


def main():
    H, N = MI()
    A = [0] * N
    B = [0] * N
    dp = [[10**12 for i in range(H+1)]
          for i in range(N+1)]
    # dp = [0 for _ in range(H + 2)]

    for i in range(N+1):
        dp[i][0] = 0

    for i in range(N):
        A[i], B[i] = MI()
        # AB[i] = (A / B, A, B)

    for i in range(N):
        # dp_tmp = [0] * (H + 2)
        for h in range(H+1):
            if h - A[i] >= 0:
                dp[i+1][h] = min(dp[i+1][h-A[i]] + B[i], dp[i][h])
            else:
                dp[i+1][h] = min(dp[i][h], B[i])

    print(dp[N][-1])


if __name__ == '__main__':
    main()
