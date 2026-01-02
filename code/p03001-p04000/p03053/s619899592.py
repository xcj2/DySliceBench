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
import copy

def grid_wall(grid, h, w, wall='#'):
    G = [[wall]*(w+2) for _ in range(h+2)]
    for hi in range(h):
        G[hi+1][1:w+1] = grid[hi]
    return G

def solve():
    H, W = MI()
    g = [[] for _ in range(H)]
    start = []
    white_cnt = 0
    for i in range(H):
        line = LS()
        for j, l in enumerate(line):
            if l == '.': white_cnt = white_cnt + 1
            else: start.append((i+1, j+1))
        g[i] = line

    if white_cnt == 0:
        print(0)
        return 

    G = grid_wall(g, H, W, 'x')
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ans = 0
    while 1:
        next = []
        for x, y in start:
            for dx, dy in move:
                nx, ny = x+dx, y+dy
                if G[nx][ny] == 'x': continue
                elif G[nx][ny] == '#': continue
                elif G[nx][ny] == '.':
                    white_cnt -= 1
                    G[nx][ny] = '#'
                    next.append((nx, ny))
        ans += 1
        # print(G)
        if white_cnt <= 0:
            print(ans)
            return
        start = next[:]



if __name__ == '__main__':
    solve()
