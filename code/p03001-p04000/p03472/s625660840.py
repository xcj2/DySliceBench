from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, accumulate
import itertools
import heapq
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


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat[i])


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


def main():
    N, H = MI()
    a = []
    b = []

    for i in range(N):
        _a, _b = MI()
        heappush(b, -1 * _b)
        heappush(a, -1 * _a)

    largest_a = -1 * heappop(a)
    count = 0

    while H > 0:
        damage = -1 * heappop(b)
        if largest_a > damage:
            break

        H -= damage
        count += 1

        if len(b) == 0:
            break

    H = max(H, 0)
    # print(count)
    # print((H + largest_a - 1) // largest_a)

    print((H + largest_a - 1) // largest_a + count)


if __name__ == '__main__':
    main()
