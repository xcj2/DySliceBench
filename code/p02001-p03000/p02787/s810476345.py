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


# 個数制限付きナップザック問題
def main():
    H, N = MI()
    A = [0] * N
    B = [0] * N
    dp = [IINF] * (H+1)
    dp[0] = 0

    for i in range(N):
        A[i], B[i] = MI()

    for i in range(N):
        dp_next = [IINF] * (H+1)
        for j in range(H+1):
            dp_next[j] = min(dp_next[j], dp[j])
            if j + A[i] <= H:
                # print(j, dp_next[j + A[i]], dp[j + A[i]], dp[j] + B[i], dp_next[j] + B[i])
                dp_next[j + A[i]] = min(dp_next[j + A[i]], dp[j + A[i]], dp[j] + B[i], dp_next[j] + B[i])
            else:
                # print(j, dp_next[H], dp[H], dp[j] + B[i], dp_next[j] + B[i])
                dp_next[H] = min(dp_next[H], dp[H], dp[j] + B[i], dp_next[j] + B[i])
        dp = dp_next
        # print(dp_next)
    print(dp[H])



if __name__ == '__main__':
    main()
