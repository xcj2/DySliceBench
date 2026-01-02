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
    N, W = MI()
    V = 10 ** 3 * N
    dp = [IINF] * (V + 1)
    w = [0] * N
    v = [0] * N
    dp[0] = 0

    for i in range(N):
        w[i], v[i] = MI()

    for i in range(N):
        dp_next = [IINF] * (V + 1)
        for j in range(V+1):
            dp_next[j] = min(dp_next[j], dp[j])
            if j + v[i] <= V:
                dp_next[j+v[i]] = min(dp[j] + w[i], dp_next[j+v[i]])
        #     print(dp_next)
        # print('===========')
        dp = dp_next

    ans = 0
    for i in range(V+1):
        if dp[i] != IINF and dp[i] <= W:
            ans = i

    print(ans)


if __name__ == '__main__':
    main()
