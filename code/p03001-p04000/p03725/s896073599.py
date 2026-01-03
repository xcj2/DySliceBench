import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

# まずK回移動する
# 後は直前に開いた扉を進んでいけるので，辺への最短路を進む

H,W,K = LI()
A = [list(input()) for _ in range(H)]

s = (-1,-1)
for i in range(H):
    for j in range(W):
        if A[i][j] == 'S':
            s = (i,j)

def grid_bfs(S,s,default=-1):
    dist = [[default]*W for _ in range(H)]
    can_visit_mark = ['.','S']
    if S[s[0]][s[1]] not in can_visit_mark:
        return dist
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    dist[s[0]][s[1]] = 0
    q = [s]
    counter = 1
    while q:
        q1 = []
        for now in q:
            for delta in d:
                new = (now[0]+delta[0], now[1]+delta[1])
                if 0 <= new[0] <= H-1 and 0 <= new[1] <= W-1:
                    if S[new[0]][new[1]] in can_visit_mark:  
                        if dist[new[0]][new[1]] == -1:
                            dist[new[0]][new[1]] = counter
                            q1.append(new)
        q = q1
        counter += 1
        if counter == K+1:
            break
    return dist

dist = grid_bfs(A,s)

min_ = float('inf')
for i in range(H):
    for j in range(W):
        if dist[i][j] != -1:
            temp = min(i,H-i-1,j,W-j-1)
            if temp < min_:
                min_ = temp

print(1+math.ceil(min_/K))