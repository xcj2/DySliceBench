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
    N, P = MI()
    s = list(map(int, S()[::-1]))
    ans = 0
    sum_of_d = 0
    cnts = [0] * P
    cnts[0] = 1
    A = [0] * N
    D = [0] * N

    if P == 2 or P == 5:
        for i in range(N):
            if s[i] % P == 0:
                ans += N - i
        print(ans)
        return

    for i in range(N):
        d = s[i] * pow(10, i, P)
        A[i] = d % P
        if i == 0:
            D[i] = A[i]
        else:
            D[i] = (D[i-1] + A[i]) % P
        # sum_of_d = (sum_of_d + d) % p
        # cnts[sum_of_d] += 1

    for d in D:
        cnts[d] += 1

    for i in cnts:
        ans += i * (i - 1) // 2

    print(ans)


if __name__ == '__main__':
    main()
