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
   

H, W = LI()
A = []
for _ in range(H):
    A.append(S())
seen = [[0 for _ in range(W)] for __ in range(H)]

def main():
    q = deque()
    ans = 0
    for i, cc in enumerate(A):
        for j, c in enumerate(cc):
            if c == '#':
                q.append((i, j, 0))
                seen[i][j] = 1
    while q:
        cur_row, cur_col, num = q.popleft()
        for dr, dc in zip(DR, DC):
            n_row = cur_row + dr
            n_col = cur_col + dc
            if not (0 <= n_row < H and 0 <= n_col < W):
                continue
            if seen[n_row][n_col]:
                continue
            if A[n_row][n_col] == '#':
                continue
            q.append((n_row, n_col, num + 1))
            seen[n_row][n_col] = 1
            ans = max(ans, num + 1)
    print(ans)

main()

