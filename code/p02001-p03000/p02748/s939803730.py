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


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat)


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


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

show_flg = False
# show_flg = True


def main():
    A, B, M = MI()
    a = LI()
    b = LI()
    x = [0] * M
    y = [0] * M
    c = [0] * M
    ans = 10**9
    # min_x_i = 10**9
    # min_y_i = 10**9
    # min_x = 10**9
    # min_y = 10**9

    for i in range(M):
        x[i], y[i], c[i] = MI()

    for i in range(M):
        A = a[x[i]-1]
        B = b[y[i]-1]
        ans = min(ans, A + B - c[i])
        # if min_x > x[i]:
        #     min_x = x[i]
        #     min_x_i = i

        # if min_y > y[i]:
        #     min_y = y[i]
        #     min_y_i = i

    ans = min(ans, min(a) + min(b))

    print(ans)


if __name__ == '__main__':
    main()
