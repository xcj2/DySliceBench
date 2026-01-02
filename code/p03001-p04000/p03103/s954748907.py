from math import factorial
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


def MS(): return map(str, input().split())


YN = ['No', 'Yes']
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = False
show_flg = True

p = None
XY = None
N = None


def main():
    N, M = MI()
    AB = [None] * N

    for i in range(N):
        A, B = MI()
        AB[i] = (A, B)

    AB = sorted(AB)

    ans = 0
    total = 0

    for i in range(N):
        price = AB[i][0]
        size = AB[i][1]

        if M < total + size:
            n = M - total
            ans += price * n
            total += n
        else:
            ans += price * size
            total += size

        if total >= M:
            break

    print(ans)


if __name__ == '__main__':
    main()
