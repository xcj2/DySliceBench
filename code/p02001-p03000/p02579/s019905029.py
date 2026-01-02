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
from collections import deque, defaultdict
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right
from copy import deepcopy

def grid_wall(grid, h, w, wall='#'):
    G = [[wall]*(w+2) for _ in range(h+2)]
    for hi in range(h):
        G[hi+1][1:w+1] = grid[hi]
    return G

def solve():
    H, W = MI()
    ch, cw = MI()
    dh, dw = MI()
    G = LLS(H)
    GW = grid_wall(G, H, W)
    GW[dh][dw] = 'G'
    # print(GW)

    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    used = deepcopy(GW)
    used[ch][cw] = '#'
    d = deque([(0, ch, cw, used)])

# for _ in range(5):
    while d:
        # print(d)
        tmp2 = []
        while d:
            m, h, w, u = d.popleft()

            for dh in range(-2, 3):
                for dw in range(-2, 3):
                    nh, nw = dh+h, dw+w
                    if not 0 <= nh <= H or not 0 <= nw <= W:
                        continue
                    if u[nh][nw] == '#':
                        continue

                    if (dh, dw) in move:
                        # print(nh, nw)
                        if u[nh][nw] == '#':
                            continue
                        elif u[nh][nw] == 'G':
                            print(m)
                            return
                        d.append((m, nh, nw, u))
                        u[nh][nw] = '#'
                        continue

                    if u[nh][nw] == '#':
                        continue
                    # elif u[nh][nw] == 'G':
                    #     print(mp)
                    #     return
                    tmp2.append((m+1, nh, nw))

        # print(tmp2)
        # mp = mp + 1
        for mm, nh, nw in tmp2:
            if u[nh][nw] == '#':
                continue
            elif u[nh][nw] == 'G':
                print(mm)
                return
            u[nh][nw] = '#'
            d.append((mm, nh, nw, u))

    print(-1)

if __name__ == '__main__':
    solve()

