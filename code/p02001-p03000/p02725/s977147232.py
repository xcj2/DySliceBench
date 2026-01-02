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


def main():
    K, N = MI()
    A = LI()
    A.append(A[-1] + (K - A[-1]) + A[0])
    N = N + 1
    diff_sum = 0
    diff = -1
    target = -1

    for i in range(N-1):
        v = abs(A[i] - A[i+1])
        diff_sum += v

        if diff < v:
            diff = v
            target = i

    # print(A, diff, diff_sum, target)
    print(diff_sum - diff)

    # a = 0
    # for i in range(target+1, N-1):
    #     a += abs(A[i] - A[i+1])
    #     print('a', a, i, i + 1)

    # for i in range(0, target):
    #     a += abs(A[i] - A[i+1])
    #     print('a', a, i, i + 1)

    # b = 0
    # for i in range(target, 0, -1):
    #     b += abs(A[i] - A[i-1])
    #     print('b', i, i - 1)

    # for i in range(N-1, target+1, -1):
    #     b += abs(A[i] - A[i-1])
    #     print('b', i, i - 1)

    # print(a, b)
    # print(min(a, b))


if __name__ == '__main__':
    main()
