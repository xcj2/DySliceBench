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
    N, M = MI()
    jobs = {}
    ans = 0

    for i in range(N):
        A, B = MI()
        if A not in jobs:
            jobs[A] = []
        jobs[A].append(B)

    h = []
    remaining_days = 1
    while remaining_days <= M:
        if remaining_days in jobs:
            for rewards in jobs[remaining_days]:
                heappush(h, -rewards)

        if len(h) > 0:
            rewards = heappop(h)
            ans += -rewards
        remaining_days += 1

    print(ans)


if __name__ == '__main__':
    main()
