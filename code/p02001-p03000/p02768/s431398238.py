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

def f(n):
    r = (n - 2)
    m = (4 * (1 - 2 ** r)) // (1 - 2)
    return (3 + m) % MOD


def modinv(a):
    return pow(a, MOD-2, MOD)


def main():
    n, a, b = MI()
    M = 10**5
    # cans = []

    # for i in range(2, M + 1):
    #     g1.append((g1[-1] * i) % MOD)
    #     inverse.append((-inverse[MOD % i] * (MOD//i)) % MOD)
    #     g2.append((g2[-1] * inverse[-1]) % MOD)

    # first = cmb(n, a, MOD)
    # second = cmb(n, b, MOD)

    # for i in range(2, n+1):
    #     ans = 0
    #     red = 0
    #     for j in range(1, i+1):
    #         if j != a and j != b:
    #             ans += cmb(i, j, MOD)
    #         else:
    #             red += cmb(i, j, MOD)
    #         # print('cmb', i, j, cmb(i, j, MOD))
    #     print(i, ans, red, 'f', f(i))
    #     cans.append(ans)
        # print('ans', f(i))

    # for i in range(len(cans) - 1):
    #     print(cans[i+1] - cans[i])

    p = 1
    c = 1
    for i in range(a):
        p *= (n - i)
        c *= (i + 1)
        p = p % MOD
        c = c % MOD
    first = p * modinv(c)

    p = 1
    c = 1
    for i in range(b):
        p *= (n - i)
        c *= (i + 1)
        p = p % MOD
        c = c % MOD
    second = p * modinv(c)
    # print(first, second)

    ans = f(n)
    print((ans - first - second) % MOD)


if __name__ == '__main__':
    main()
