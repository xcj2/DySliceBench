import sys
sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())
def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())
def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def MS(): return input().split()
def LS(): return list(input())
def LLS(rows_number): return [LS() for _ in range(rows_number)]
def printlist(lst, k=' '): print(k.join(list(map(str, lst))))
INF = float('inf')
# from math import ceil, floor, log2
from collections import deque
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np
# from numpy import cumsum  # accumulate
# from pprint import pprint

def grid_wall(grid, h, w, wall='#'):
    G = [[wall]*(w+2) for _ in range(h+2)]
    for hi in range(h):
        G[hi+1][1:w+1] = grid[hi]
    return G

def solve():
    H, W = MI()
    G = LLS(H)

    black_cnt = 0
    for i in range(H):
        for j in range(W):
            if G[i][j] == '#':
                black_cnt += 1
    # print(black_cnt)

    G[-1][-1] = 'G'
    G[0][0] = '#'

    G2 = grid_wall(G, H, W, '#')
    # print(np.array(G2))

    q = deque([(1, 1, 1)])
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    cost = INF
    while q:
        x, y, d = q.popleft()
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if G2[nx][ny] == 'G':
                cost = min(cost, d + 1)
            elif G2[nx][ny] == '#': continue
            else:
                q.append((nx, ny, d+1))
                G2[nx][ny] = '#'
    if cost == INF:
        print(-1)
        return
    # print(cost)
    print(H * W - black_cnt - cost)
if __name__ == '__main__':
    solve()
