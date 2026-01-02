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

BLOCK = '#'
ROAD = '.'


def bfs(graph, initial, goal, H, W):
    options = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = deque([initial])
    visited = [[False for i in range(W)] for i in range(H)]
    dist = [[-1 for i in range(W)] for i in range(H)]
    visited[initial[0]][initial[1]] = True
    dist[initial[0]][initial[1]] = 0

    while len(q) != 0:
        p = q.popleft()

        for d in options:
            i = p[0] + d[0]
            j = p[1] + d[1]

            if i >= 0 and i < H and j >= 0 and j < W and not visited[i][j] and graph[i][j] != BLOCK:
                visited[i][j] = True
                q.append((i, j))
                dist[i][j] = dist[p[0]][p[1]] + 1

    return dist


def main():
    H, W = MI()
    graph = [None] * H

    for i in range(H):
        graph[i] = list(S())

    dist = bfs(graph, (0, 0), (H-1, W-1), H, W)

    if dist[H-1][W-1] == -1:
        print(-1)
        return

    ans = H * W
    # print_matrix(dist)
    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#':
                ans -= 1

    ans -= dist[H-1][W-1] + 1
    print(ans)


if __name__ == '__main__':
    main()
