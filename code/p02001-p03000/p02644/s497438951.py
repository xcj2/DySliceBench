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

H,W,K = LI()
x1,y1,x2,y2 = LI()
c = [list(map(str,input())) for _ in range(H)]

def grid_bfs(S,s,default=-1):
    dist = [[default]*W for _ in range(H)]
    can_visit_mark = ['.']
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    dist[s[0]][s[1]] = 0
    q = [s]
    counter = 1
    while q:
        q1 = []
        for now in q:
            for delta in d:
                for i in range(1,K+1):
                    new = (now[0]+i*delta[0], now[1]+i*delta[1])
                    if 0 <= new[0] <= H-1 and 0 <= new[1] <= W-1:
                        if S[new[0]][new[1]] in can_visit_mark:  
                            if dist[new[0]][new[1]] == default:
                                dist[new[0]][new[1]] = counter
                                q1.append(new)
                            elif dist[now[0]][now[1]] < dist[new[0]][new[1]]:
                                continue
                            else:
                                break
                        else:
                            break
                    else:
                        break
        if dist[x2-1][y2-1] != default:
            return dist[x2-1][y2-1]
        q = q1
        counter += 1
    return -1

print(grid_bfs(c,(x1-1,y1-1)))