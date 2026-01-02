from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate, product, combinations_with_replacement
import sys
import bisect
import string
import math
import time
from decimal import *


def I(): return int(input())
def S(): return input()
def MI(): return map(int, input().split())
def MS(): return map(str, input().split())
def LI(): return [int(i) for i in input().split()]
def LI_(): return [int(i)-1 for i in input().split()]
def StoI(): return [ord(i)-97 for i in input()]
def ItoS(nn): return chr(nn+97)
def input(): return sys.stdin.readline().rstrip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def print_matrix(mat):
    for i in range(len(mat)):
        print(*['IINF' if v == IINF else "{:0=4}".format(v) for v in mat[i]])


yn = {False: 'No', True: 'Yes'}
YN = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
show_flg = False
# show_flg = True

def pl(x, d):
        return x - d - 0.5


def pr(x, d):
    return x + d + 0.5


def b(A, K):
    for k in range(K):
        ans = []
        for i in range(len(A)):
            c = 0
            for j in range(len(A)):
                l = pl(j, A[j])
                r = pr(j, A[j])

                if i >= l and i <= r:
                    c += 1
            ans.append(c)
        A = ans
        if ans[-1] == len(A):
            print(k, ans)
            return ans
    return A

def main():
    N, K = MI()
    A = LI()

    for i in range(min(100, K)):
        B = [0] * N
        for i in range(N):
            l = max(0, i - A[i])
            r = min(N - 1, i + A[i])
            B[l] += 1
            if r+1 < N:
                B[r+1] -= 1

        for i in range(1, N):
            B[i] += B[i-1]
        A = B

    print(*A)
    # N = 100000
    # A = [0] * N
    # l_arr = []
    # r_arr = []

    # print(b(A, K))

    # for i in range(N):
    #     l = pl(i, A[i])
    #     r = pr(i, A[i])
    #     l_arr.append((l, r))
    #     r_arr.append((r, l))
    #     # c = r - l
    #     # v.append(math.ceil(c))
    #     # print(i+1, 'left', pl(i+1, A[i]), 'right', pr(i+1, A[i]))

    # l_arr.sort()
    # r_arr.sort()
    # # print('l_arr', l_arr)
    # # print('r_arr', r_arr)

    # ans = [0] * N

    # for k in range(min(41, K)):
    #     nl_arr = []
    #     nr_arr = []
    #     for i in range(N):
    #         l_idx = bisect.bisect_right(l_arr, (i, None))
    #         r_idx = bisect.bisect_right(r_arr, (i, None))
    #         ans[i] = l_idx - r_idx
    #         l = pl(i, ans[i])
    #         r = pr(i, ans[i])
    #         nl_arr.append((l, r))
    #         nr_arr.append((r, l))

    #     nl_arr.sort()
    #     nr_arr.sort()
    #     l_arr = nl_arr
    #     r_arr = nr_arr

        # print(k, ans[-1])
        # print(idx, l_arr[idx])
        # print(*ans)
    # print(*A)
    # print(k)
    # print(*ans)


if __name__ == '__main__':
    main()
