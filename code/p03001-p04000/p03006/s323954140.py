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


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat[i])


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

def cost(x, y, initial, N):
    a = x[initial]
    b = y[initial]
    for i in range(N):
        if i == initial:
            continue

    return 0


def main():
    N = I()
    x = [0] * N
    y = [0] * N
    ans = 0
    dist = [[None] * N for i in range(N)]

    if N == 1:
        print(1)
        return

    for i in range(N):
        x[i], y[i] = MI()

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            dist[i][j] = str(x[j] - x[i]) + "," + str(y[j] - y[i])

    # print_matrix(dist)

    c = defaultdict(int)
    ans = 1
    for i in range(N):
        for j in range(N):
            if dist[i][j] == None:
                continue
            c[dist[i][j]] += 1

    mcost = max(c.values())
    print(N - mcost)


if __name__ == '__main__':
    main()
