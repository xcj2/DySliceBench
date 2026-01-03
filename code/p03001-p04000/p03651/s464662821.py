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


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_n(a, n):
    ans = a[0]
    for i in range(1, n):
        ans = gcd(ans, a[i])
    return ans


def main():
    N, K = MI()
    A = LI()
    A = sorted(A)
    mx = max(A)

    ret = gcd_n(A, N)

    if mx < K:
        print('IMPOSSIBLE')
        return

    if K % ret == 0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')

    # A = set(A)
    # while True:
    #     c = len(A)
    #     for p in combinations(A, 2):
    #         A.add(abs(p[0] - p[1]))

    #     if c == len(A):
    #         break

    # print(A)

if __name__ == '__main__':
    main()
