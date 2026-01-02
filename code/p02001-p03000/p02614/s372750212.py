from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate, product, combinations_with_replacement
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
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def print_matrix(mat):
    for i in range(len(mat)):
        print(*['IINF' if v == IINF else "{:0=4}".format(v) for v in mat[i]])


yn = {False: 'No', True: 'Yes'}
YN = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
show_flg = False
# show_flg = True


def main():
    H, W, K = MI()
    graph = [None] * H
    black_cnt = 0
    dic = defaultdict(int)
    ans = 0

    for i in range(H):
        s = S()
        graph[i] = s

        for j in range(len(s)):
            if s[j] == '#':
                dic[(i, j)] += 1
                black_cnt += 1

    N = H + W
    for i in range(2 ** N):
        row = []
        col = []
        for j in range(N):
            if ((i >> j) & 1):
                if j < H:
                    row.append(j)
                else:
                    col.append(j - H)

        current_cnt = black_cnt
        visited = defaultdict(int)
        for i in row:
            for j in range(W):
                visited[(i, j)] += 1
                if (i,j) in dic:
                    current_cnt -= 1

        for i in range(H):
            for j in col:
                if (i,j) in visited:
                    continue
                visited[(i, j)] += 1
                if (i,j) in dic:
                    current_cnt -= 1

        if current_cnt == K:
            ans += 1
        # print('row', row)
        # print('col', col)

    print(ans)

if __name__ == '__main__':
    main()
