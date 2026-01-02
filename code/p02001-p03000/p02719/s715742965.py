from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate
import sys
import bisect
import string
import math
import time
import random


def I(): return int(input())


def S(): return input()


def MI(): return map(int, input().split())


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


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
    N, K = MI()
    v = min(N % K, abs(N % K - K))
    print(v)
    # a = N

    # for i in range(100):
    #     N = random.randint(0, 10**5)
    #     K = random.randint(0, 10**5)
    #     a = N
    #     ans = 10**19
    #     for j in range(10**5):
    #         a = abs(a - K)
    #         ans = min(ans, a)

        # if v == ans:
        #     print('Yes')

        # for j in range(10**5):
        #     if N >= K:
        #         N = N % K
        #     else:
        #         K = K % N
        # print(N, K)



if __name__ == '__main__':
    main()
