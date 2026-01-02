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


def lcm(a, b):
    return a*b // gcd(a, b)


def lcm_n(A, N):
    # A = sorted(A)
    ans = A[0]
    # for i in range(1, N):
    #     ans = fractions.gcd(A[i], ans)
    for i in range(1, N):
        ans = lcm(ans, A[i])
    return ans


def main():
    N, M = MI()
    a = LI()

    if any([i % 2 for i in a]):
        print(0)
        return

    n = lcm_n(a, N)
    n = n // 2

    if not all([(2 * n // x) % 2 for x in a]):
        print(0)
        return

    if n > M:
        print(0)
    else:
        t = M // n
        if t % 2 == 0:
            t -= 1
        print(t // 2 + 1)


if __name__ == '__main__':
    main()
