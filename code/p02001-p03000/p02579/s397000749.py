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

H,W = LI()
Ch,Cw = LI()
Dh,Dw = LI()

Q = [list(map(str,input())) for _ in range(H)]
D = [(0,1),(0,-1),(-1,0),(1,0)]

visited = [[-1]*W for _ in range(H)]

s = (Ch-1,Cw-1)
c = 0
visited[Ch-1][Cw-1] = c
S = [s]
Sc = [s]
while True:
    while S:
        v = S.pop()
        for d in D:
            new = (v[0]+d[0],v[1]+d[1])
            if new[0] == Dh-1 and new[1] == Dw-1:
                print(c)
                exit()
            if 0 <= new[0] < H and 0 <= new[1] < W and Q[new[0]][new[1]] == '.' and visited[new[0]][new[1]] == -1:
                visited[new[0]][new[1]] = c
                S.append(new)
                Sc.append(new)
    c += 1
    S = []
    for v in Sc:
        for i in range(-2,3):
            for j in range(-2,3):
                new = (v[0]+i,v[1]+j)
                if new[0] == Dh-1 and new[1] == Dw-1:
                    print(c)
                    exit()
                if 0 <= new[0] < H and 0 <= new[1] < W and visited[new[0]][new[1]] == -1 and Q[new[0]][new[1]] == '.':
                    S.append(new)
                    visited[new[0]][new[1]] = c
    if not S:
        break
    Sc = S[:]
    
print(-1)