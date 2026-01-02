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

g = []


def rec(i, s, N):
    # print(s)
    global g
    g.append(int(s))
    if len(s) > N:
        return

    if i - 1 >= 0:
        rec(i-1, s + str(i-1), N)
    rec(i, s + str(i), N)
    if i + 1 <= 9:
        rec(i+1, s + str(i+1), N)


def main():
    global g
    K = I()
    ans = []

    for i in range(1, 10):
        rec(i, str(i), 11)
    g = sorted(g)
    # print(len(g))
    print(g[K-1])


if __name__ == '__main__':
    main()
