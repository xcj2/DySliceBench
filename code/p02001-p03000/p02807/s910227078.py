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

show_flg = False
# show_flg = True


def modinv(a):
    return pow(a, MOD-2, MOD)


def main():
    N = I()
    x = LI()
    distance = [(x[i] - x[i-1]) % MOD for i in range(1, N)]

    F = 1
    for i in range(1, N):
        F *= i
        F %= MOD

    c = [0] * (N - 1)
    for i in range(N-1):
        if i == 0:
            c[i] = (F * 1) % MOD
        else:
            c[i] = (F * modinv(i+1)) % MOD + c[i-1]

    moves = [(d * e) % MOD for d, e in zip(distance, c)]
    print(sum(moves) % MOD)


if __name__ == '__main__':
    main()
