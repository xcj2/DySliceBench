import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def solve(maze, st_tuple):
    st_row, st_col = st_tuple
    W, H = len(maze[0]), len(maze)
    visited = [[0 for _ in range(W)] for __ in range(H)]
    steps = [[0 for _ in range(W)] for __ in range(H)]
    q = deque()
    q.append((st_row, st_col, 0))
    visited[st_row][st_col] = 1
    steps[st_row][st_col] = 0
    while q:
        cur_row, cur_col, count = q.popleft()
        for dr, dc in zip(DR, DC):
            next_row = cur_row + dr
            next_col = cur_col + dc
            if 0 <= next_row < H and 0 <= next_col < W:
                pass
            else:
                continue
            if maze[next_row][next_col] == '#':
                continue
            if visited[next_row][next_col]:
                continue
            q.append((next_row, next_col, count + 1))
            visited[next_row][next_col] = 1
            steps[next_row][next_col] = count + 1
    max_count = 0
    for r in range(H):
        for c in range(W):
            max_count = max(max_count, steps[r][c])
    return max_count

def main():
    H, W = LI()
    maze = []
    for _ in range(H):
        maze.append(S())
    num = 0
    axes = [(s_r, s_c) for s_r in range(H) for s_c in range(W)]
    for st_row, st_col in axes:
        if maze[st_row][st_col] == '#':
            continue
        a = solve(maze, (st_row, st_col))
        num = max(num, a)
    print(num)
main()

