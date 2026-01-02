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


def main():
    N, M = MI()
    A = LI()
    D = {}

    for i in range(M):
        B, C = MI()
        if C not in D:
            D[C] = 0
        D[C] += B

    for i in range(N):
        if A[i] not in D:
            D[A[i]] = 0
        D[A[i]] += 1

    sorted_items = sorted(D.items(), reverse=True)
    total = 0
    ans = 0
    for integer, num in sorted_items:
        if total + num > N:
            ans += integer * (N - total)
            total = N
            break
        else:
            total += num
            ans += integer * num

    print(ans)


if __name__ == '__main__':
    main()
