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
    s = S()
    t = S()
    s_len = len(s)
    t_len = len(t)
    dp = [[0] * (t_len+1) for i in range(s_len+1)]
    ans = []

    for i in range(s_len):
        for j in range(t_len):
            if s[i] == t[j]:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])

    # print(*dp)
    i = s_len
    j = t_len
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            ans.append(s[i-1])
            i -= 1
            j -= 1

    print(''.join(ans[::-1]))

if __name__ == '__main__':
    main()
