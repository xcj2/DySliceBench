from sys import stdin
import sys
import numpy as np
import collections
from functools import cmp_to_key
import heapq

##  input functions for me
def rsa(sep = ''):
    if sep == '' :
        return input().split() 
    else: return input().split(sep)
def rip(sep = ''):
    if sep == '' :
        return map(int, input().split()) 
    else: return map(int, input().split(sep))
def ria(sep = ''): 
    return list(rip(sep))
def ri(): return int(input())
def rd(): return float(input())
def rs(): return input()
##

def in_range(t, l, r):
    return l <= t and t < r

def main():
    H, W = rip()
    S = [""] * H
    for i in range(H): S[i] = rs()

    inf = int(1e9)
    ma = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#': continue

            mi = [[inf] * W for i in range(H)]
            mi[i][j] = 0
            q = collections.deque()
            q.append((i,j))
            while len(q) > 0:
                y, x = q.popleft()
                for t in range(4):
                    ny = y + dy[t]
                    nx = x + dx[t]
                    if (not in_range(nx, 0, W)) or (not in_range(ny, 0, H)) : continue
                    if S[ny][nx] == '#': continue
                    if mi[ny][nx] == inf:
                        mi[ny][nx] = mi[y][x] + 1
                        q.append((ny, nx))
            for k in range(H):
                for l in range(W):
                    if S[k][l] == '#': continue
                    ma = max(ma, mi[k][l])
    
    print(ma)




if __name__ == "__main__":
    main()
