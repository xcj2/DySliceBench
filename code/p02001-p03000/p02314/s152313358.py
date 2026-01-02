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


def S(): return input()


def MI(): return map(int, input().split())


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def make4(initial, L, M, N, O):
    return [[[[initial for i in range(O)]
                for n in range(N)]
                for m in range(M)]
                for l in range(L)]


def make3(initial, L, M, N):
    return [[[initial for n in range(N)]
                for m in range(M)]
                for l in range(L)]


def debug(table, *args):
    ret = []
    for name, val in table.items():
        if val in args:
            ret.append('{}: {}'.format(name, val))
    print(' | '.join(ret), file=sys.stderr)


yn = {False: 'No', True: 'Yes'}
YN = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def main():
    n, m = MI()
    c = LI()
    dp = [[IINF] * (n+1) for i in range(m+1)]
    dp[0][0] = 0

    for i in range(m):
        for j in range(n+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            if j + c[i] <= n:
                dp[i][j+c[i]] = min(dp[i][j+c[i]], dp[i][j] + 1)
                dp[i+1][j+c[i]] = min(dp[i+1][j+c[i]], dp[i][j] + 1)
    print(dp[m][n])

if __name__ == '__main__':
    main()

