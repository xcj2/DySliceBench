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

def f(x):
    return x


# 二分探索 ok ng
def main():
    N = I()
    L = LI()
    # L = L.sort()
    R = sorted(L, reverse=True)
    L = R[::-1]
    # print(R)
    ans = 0

    for i in range(N):
        for j in range(i+1, N):
            a = R[i]
            b = R[j]
            remain = a - b + 1
            idx = bisect.bisect_left(L, remain)
            c_idx = N - (idx + 1)
            if j < c_idx:
                c = (c_idx - j)
                ans += c
                # print('Need', remain, 'c', c)
                # print('a', a)
                # print('b', b)
                # print(i, j, c_idx - j)
                # print('a', a, 'b', b, c_idx, L[:idx])

    print(ans)


if __name__ == '__main__':
    main()
