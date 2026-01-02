import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

def bfs(A):
    d = [[0,1],[0,-1],[1,0],[-1,0]]
    used = [[False]*W for _ in range(H)]
    q = []
    for i in range(H):
        for j in range(W):
            if A[i][j] == '#':
                used[i][j] = True
                q.append([i,j])
    c = 0
    while q:
        q1 = []
        count_flag = False
        for place in q:
            for move in d:
                new_x, new_y = place[0]+move[0], place[1]+move[1]
                if 0<=new_x<H and 0<=new_y<W:
                    if used[new_x][new_y]==False:
                        used[new_x][new_y] = True
                        q1.append([new_x,new_y])
                        count_flag = True
        q = q1
        if count_flag:
            c += 1
    return c

H,W = II()
A = [list(map(str, input())) for _ in range(H)]
print(bfs(A))