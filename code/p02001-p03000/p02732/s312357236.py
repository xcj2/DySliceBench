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


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat[i])


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


def cmb(n, r):
    p = 1
    c = 1
    for i in range(r):
        p *= (n - i)
        c *= (i + 1)
    return p // c


def main():
    N = I()
    A = LI()
    a = Counter(A)
    c = 0
    org = {}
    one = {}
    org_tital = 0
    for k, v in a.items():
        org[k] = cmb(v, 2)
        one[k] = cmb(v-1, 2)
        org_tital += org[k]

    # print(org, one, org_tital)

    for i in range(N):
        diff = org[A[i]] - one[A[i]]
        print(org_tital - diff)
    # print()


if __name__ == '__main__':
    main()
