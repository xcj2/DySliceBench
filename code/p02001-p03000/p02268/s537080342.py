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


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat[i])


YNL = {False: 'No', True: 'Yes'}
YNU = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = True
show_flg = False


def f(a, x):
    return a[x]


# 二分探索 ok ng
def main():
    N = I()
    S = LI()
    Q = I()
    T = LI()
    ans = 0

    for i in range(Q):
        s = 0
        t = N
        ok = s - 1
        ng = t
        target = T[i]
        while ng - ok > 1:
            mid = (ng + ok) // 2
            # print(mid, S[mid], target)
            if f(S, mid) <= target:
                ok = mid
            else:
                ng = mid

        ans += 1 if target == S[ok] else 0

    print(ans)


if __name__ == '__main__':
    main()

