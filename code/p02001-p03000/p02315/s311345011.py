from bisect import bisect_left as lower_bound
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


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YN = ['No', 'Yes']
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
    N, W = MI()
    v = [0] * N
    w = [0] * N
    dp = [0] * (W + 1)

    for i in range(N):
        v[i], w[i] = MI()

    for i in range(N):
        dp_next = [0] * (W + 1)
        for j in range(W):
            dp_next[j] = max(dp[j], dp_next[j])
            if j+w[i] <= W:
                dp_next[j+w[i]] = max(dp[j+w[i]], dp[j] + v[i])
        dp = dp_next
        # print(dp)

    print(dp[W])


if __name__ == '__main__':
    main()

