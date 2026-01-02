from decimal import *
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


YNL = {False: 'No', True: 'Yes'}
YNU = {False: 'NO', True: 'YES'}
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

BLOCK = '#'
ROAD = '.'


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat[i])


def main():
    H, W = MI()
    graph = [None] * H

    for i in range(H):
        graph[i] = list(S())

    dp = [[IINF] * W for i in range(H)]
    dp[0][0] = 0 if graph[0][0] == ROAD else 1

    for i in range(H):
        for j in range(W):
            for p in [(1, 0), (0, 1)]:
                ni = i + p[0]
                nj = j + p[1]
                if ni >= 0 and ni < H and nj >= 0 and nj < W:
                    cost = 0
                    if graph[i][j] == ROAD and graph[ni][nj] == BLOCK:
                        cost = dp[i][j] + 1
                    else:
                        cost = dp[i][j]
                    dp[ni][nj] = min(cost, dp[ni][nj])

    # print_matrix(dp)
    print(dp[H-1][W-1])


if __name__ == '__main__':
    main()
