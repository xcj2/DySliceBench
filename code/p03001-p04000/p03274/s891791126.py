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


def main():
    N, K = MI()
    x = LI()
    x.append(0)
    x.sort()

    for i in range(N+1):
        if x[i] == 0:
            zero_index = i

    ans = 10**9

    for i in range(N+1):
        # print(i, zero_index, i <= zero_index, zero_index <= i + K + 1)
        if i <= zero_index and zero_index <= i + K and i + K < N + 1:
            # print(x[i:i+K+1])
            left = x[i]
            right = x[i+K]
            mn = min(abs(left), abs(right))
            ans = min(ans, abs(left) + abs(right) + mn)
            # print(left, right)
            # print(ans)

    print(ans)


if __name__ == '__main__':
    main()
