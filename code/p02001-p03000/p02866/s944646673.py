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


def main():
    MOD = 998244353
    N = I()
    D = LI()

    if D[0] != 0:
        print(0)
        return

    if any([d == 0 for d in D[1:]]):
        print(0)
        return

    MAX_D = max(D)
    node = [0] * (MAX_D + 1)

    for i in range(N):
        node[D[i]] += 1

    # print(node)
    ans = 1
    for i in range(1, len(node)):
        ans *= node[i-1] ** node[i]
        ans %= MOD
    print(ans % MOD)


if __name__ == '__main__':
    main()
