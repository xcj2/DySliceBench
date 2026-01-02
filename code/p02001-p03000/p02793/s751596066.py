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


YN = ['No', 'Yes']
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


show_flg = True
show_flg = False


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# N個の最大公約数
def eucledean(A, N):
    # A = sorted(A)
    ans = A[0]
    for i in range(1, N):
        ans = gcd(A[i], ans)
    return ans


def lcm(a, b):
    return a*b // gcd(a, b)


# N個最小公倍数
def lcm_n(A, N):
    # A = sorted(A)
    ans = A[0]
    # for i in range(1, N):
    #     ans = fractions.gcd(A[i], ans)
    for i in range(1, N):
        ans = lcm(ans, A[i])
    return ans


def modinv(a):
    return pow(a, MOD-2, MOD)


def main():
    N = I()
    A = LI()
    ans = 0

    a = lcm_n(A, N)
    a %= MOD
    for i in range(N):
        ans += a * modinv(A[i])
        ans %= MOD
    print(ans % MOD)


if __name__ == '__main__':
    main()
