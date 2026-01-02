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
        return [[] for _ in range(num)]
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

H,W = II()
S = [str(input()) for _ in range(H)]

d = [(0,1),(0,-1),(1,0),(-1,0)]
visited = [[False]*W for _ in range(H)]

ans = 0
for i in range(H):
    for j in range(W):
        if visited[i][j]:
            continue
        else:
            whites = 0
            blacks = 0
            p = [(i,j)]
            while p:
                now = p.pop()
                if S[now[0]][now[1]]=='#':
                    blacks += 1
                else:
                    whites += 1
                visited[now[0]][now[1]] = True
                for d0 in d:
                    new = (now[0]+d0[0],now[1]+d0[1])
                    if 0<=new[0]<=H-1 and 0<=new[1]<=W-1:
                        if S[now[0]][now[1]]!=S[new[0]][new[1]] and (not visited[new[0]][new[1]]):
                            p.append(new)
                            visited[new[0]][new[1]] = True
            ans += whites*blacks
print(ans)