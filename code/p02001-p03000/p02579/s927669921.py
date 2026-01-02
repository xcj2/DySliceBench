import sys
import re
import queue
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
# input = sys.stdin.readline
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    H, W = i_map()
    Ch, Cw = i_map()
    Dh, Dw = i_map()
    Ch,Cw = Ch-1,Cw-1
    Dh,Dw = Dh-1,Dw-1
    maze = [input() for _ in range(H)]

    INF = 10 ** 12
    path = [[INF] * W for _ in range(H)]  # path: 各マスへの移動コスト

    # walk:移動A, warp:移動B
    walk = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    warp = [(i, j) for i in range(-2, 3) for j in range(-2, 3) if (i, j) not in [(0, 0)] + walk]

    q = deque()
    path[Ch][Cw] = 0
    q.append((Ch, Cw, 0))

    while(q):
        ux,uy,s = q.popleft()
        for dx,dy in walk:
            nx = ux + dx
            ny = uy + dy
            if(0<=nx<H and 0<=ny<W and maze[nx][ny]=='.' and path[nx][ny] > s):
                path[nx][ny] = s
                q.appendleft((nx,ny,s))
        for dx,dy in warp:
            nx = ux + dx
            ny = uy + dy
            if(0<=nx<H and 0<=ny<W and maze[nx][ny]=='.' and path[nx][ny] > s+1):
                path[nx][ny] = s+1
                q.append((nx,ny,s+1))

    ans = path[Dh][Dw] if path[Dh][Dw] < INF else '-1'
    print(ans)


if __name__ == '__main__':
	main()