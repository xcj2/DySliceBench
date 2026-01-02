from math import factorial
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
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = False
show_flg = True


def main():
    n = '0' + S()
    N = len(n)
    n = n[::-1]
    n = [int(i) for i in n]
    dp = [[0] * 2 for i in range(N+1)]
    dp[0][1] = 1

    # print(n)
    for i in range(N):
        # print(i, 'no up', dp[i][0] + n[i], dp[i][1] + n[i] + 1)
        # print(i, 'no down', dp[i][0] + 10 - n[i], dp[i][1] + 10 - (n[i] + 1))
        dp[i+1][0] = min(dp[i][0] + n[i], dp[i][1] + n[i] + 1)
        dp[i+1][1] = min(dp[i][0] + 10 - n[i], dp[i][1] + 10 - (n[i] + 1))

    print(min(dp[N]))


if __name__ == '__main__':
    main()
