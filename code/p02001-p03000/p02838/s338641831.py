# from heapq import heappush, heappop, heapify
# from collections import deque, defaultdict, Counter
# import itertools
# from itertools import permutations, combinations, accumulate
import sys
# import bisect
# import string
# import math
# import time
# from fractions import gcd
#import random


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


# YN = ['No', 'Yes']
MOD = 10**9+7
# inf = float('inf')
# IINF = 10**10
# l_alp = string.ascii_lowercase
# u_alp = string.ascii_uppercase
# ts = time.time()
# sys.setrecursionlimit(10**6)
# nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = True
show_flg = False

# xor
# n + i = n ^ i implies n & i = 0


# def sumXOR(arr,  n):
#     _sum = 0
#     for i in range(0, 64):
#         zc = 0
#         oc = 0

#         # Individual sum at each bit position
#         idsum = 0
#         for j in range(0, n):
#             if (arr[j] % 2 == 0):
#                 zc = zc + 1
#             else:
#                 oc = oc + 1
#             arr[j] = arr[j] >> 1

#         # calculating individual bit sum
#         idsum = oc * zc * (1 << i)
#         print(zc, oc, idsum)

#         # final sum
#         _sum = _sum + idsum
#         _sum %= MOD

#     return _sum


def main():
    N = I()
    A = list(MI())
    BIT = 61
    C = [[0] * BIT for i in range(N+1)]
    pows = [pow(2, i, MOD) for i in range(BIT)]
    ans = 0

    for i in range(N):
        bit = 1
        for j in range(BIT):
            if A[i] & bit:
                C[i+1][j] = C[i][j] + 1
            else:
                C[i+1][j] = C[i][j]
            bit = bit << 1

    for i in range(N):
        bit = 1
        for j in range(BIT):
            oc = C[N][j] - C[i][j]
            # print('b', ans, i, j, bit, oc)
            if A[i] & bit:
                zc = N - i - oc
                ans += pows[j] * zc
            elif oc != 0:
                ans += pows[j] * oc
            ans %= MOD
            bit = bit << 1
            # print('a', ans, i, j, bit, oc)

    print(ans)


if __name__ == '__main__':
    main()
