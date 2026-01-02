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
# sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = True
show_flg = False


def f(a, x):
    return a[x]


def binary_search(s, t, d, target):
    ok = s - 1
    ng = t

    while ng - ok > 1:
        mid = (ng + ok) // 2
        if f(d, mid) <= target:
            ok = mid
        else:
            ng = mid

    return ok


# 二分探索 ok ng
def main():
    N = I()
    A = LI()
    B = LI()
    C = LI()
    A = sorted(A)
    C = sorted(C)
    ans = 0
    # print(A)
    # print(C)

    for i in range(N):
        a_idx = bisect.bisect_left(A, B[i])
        c_idx = bisect.bisect_right(C, B[i])
        ans += a_idx * (N - c_idx)
        # print(B[i], a_idx * (N - c_idx))
        # print(B[i], a_idx, c_idx)

    print(ans)


if __name__ == '__main__':
    main()
