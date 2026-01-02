# N個の最大公約数
# ユークリッド互除法
# Check


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a*b // gcd(a, b)


def good(A, N):
    # A = sorted(A)
    ans = A[0]
    # for i in range(1, N):
    #     ans = fractions.gcd(A[i], ans)
    for i in range(1, N):
        ans = lcm(ans, A[i])
    return ans


def my(A, N):
    A = sorted(A)

    while True:
        v = A[0]
        tmp = [v]
        for i in range(len(A)):
            if A[i] % v == 1:
                print(1)
                return
            if A[i] % v == 0:
                pass
            else:
                tmp.append(A[i] % v)

        if len(A) == 1:
            print(A[0])
            return

        A = sorted(tmp)
        # print(A)


def main():
    N = int(input())
    A = list(map(int, input().split()))
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

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    N = I()
    A = LI()
    n = A[0]

    for i in range(1, N):
        n = gcd(n, A[i])

    print(n)


if __name__ == '__main__':
    main()
