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

BLOCK = '#'
ROAD = '.'

warps = []

for i in range(-2, 3):
    for j in range(-2, 3):
        if (i, j) not in [(-1, 0), (0, 1), (1, 0), (0, -1), (0, 0)]:
            warps.append((i, j))

def bfs(graph, initial, goal, H, W):
    options = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = deque([(initial, 0)])
    visited = [[False for i in range(W)] for i in range(H)]
    dist = [[-1 for i in range(W)] for i in range(H)]
    visited[initial[0]][initial[1]] = True
    block_li = set([])

    while len(q) != 0:
        p, cnt = q.popleft()

        for d in options:
            i = p[0] + d[0]
            j = p[1] + d[1]

            if i >= 0 and i < H and j >= 0 and j < W and not visited[i][j]:
                if graph[i][j] != BLOCK:
                    visited[i][j] = True
                    q.append(((i, j), cnt))

                    if goal[0] == i and goal[1] == j:
                        return cnt
                else:
                    block_li.add((p[0], p[1]))

        if len(q) == 0 and len(block_li) != 0:
            # print(block_li)
            for bp in block_li:
                for d in warps:
                    i = bp[0] + d[0]
                    j = bp[1] + d[1]

                    if i >= 0 and i < H and j >= 0 and j < W and not visited[i][j] and graph[i][j] != BLOCK:
                        tmp = cnt + 1
                        visited[i][j] = True
                        q.append(((i, j), tmp))

                        if goal[0] == i and goal[1] == j:
                            return tmp
            block_li = set()
    return -1


def main():
    H, W = MI()
    CH, CW = MI()
    DH, DW = MI()
    graph = [None] * H
    CH -= 1
    CW -= 1
    DH -= 1
    DW -= 1

    for i in range(H):
        graph[i] = list(S())

        for j in range(W):
            if graph[i][j] == 'S':
                pass

    ret = bfs(graph, (CH, CW), (DH, DW), H, W)
    print(ret)


if __name__ == '__main__':
    main()
