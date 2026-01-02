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
        for _ in range(num): return []
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list,zip(*read_all))

#################

H,W = II()
s = [list(map(str, input())) for _ in range(H)]

w_count = 0
for i in range(H):
    for j in range(W):
        if s[i][j] == '.':
            w_count += 1


v = (0,0)
check_visited = [[False]*W for _ in range(H)]
check_visited[v[0]][v[1]] = True
S = [v]
flag = False
c = 1
while S:
    S1 = []
    for v1 in S:
        if v1[0]==H-1 and v1[1]==W-1:
            flag = True
            break
        if v1[0]-1>=0:
            if check_visited[v1[0]-1][v1[1]] == False and s[v1[0]-1][v1[1]] == '.':
                check_visited[v1[0]-1][v1[1]] = True
                S1.append((v1[0]-1,v1[1]))
        if v1[0]+1<=H-1:
            if check_visited[v1[0]+1][v1[1]] == False and s[v1[0]+1][v1[1]] == '.':
                check_visited[v1[0]+1][v1[1]] = True
                S1.append((v1[0]+1,v1[1]))
        if v1[1]-1>=0:
            if check_visited[v1[0]][v1[1]-1] == False and s[v1[0]][v1[1]-1] == '.':
                check_visited[v1[0]][v1[1]-1] = True
                S1.append((v1[0],v1[1]-1))
        if v1[1]+1<=W-1:
            if check_visited[v1[0]][v1[1]+1] == False and s[v1[0]][v1[1]+1] == '.':
                check_visited[v1[0]][v1[1]+1] = True
                S1.append((v1[0],v1[1]+1))
    else:
        S = S1
        c += 1
        continue
    break

if flag:
    print(w_count-c)
else:
    print(-1)