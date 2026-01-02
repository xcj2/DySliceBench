import sys
input=sys.stdin.readline
from collections import deque
from heapq import heappush,heappop
import re

def int_raw():
    return int(input())
 
def ss_raw():
    return input().split()
 
def ints_raw():
    return tuple(map(int, ss_raw()))


DIV = 10**9+7


def main():
    H,W = ints_raw()
    Ss = ["#"+input()[:-1]+"#" for _ in range(H)]
    W = W+2
    H = H+2
    Ss = ["#"*W]+Ss+["#"*W]
    lenHor = [[0]*W for _ in range(H)]
    lenVer = [[0]*W for _ in range(H)]
    for h,S in enumerate(Ss):
        buf = 0
        last_idx = 1
        for idx,c in enumerate(S):
            if c == '#':
                for x in range(last_idx,idx):
                    lenHor[h][x] = buf
                buf =0
                last_idx = idx+1
            else:
                buf+=1
    
    for w in range(W):
        buf = 0
        last_idx = 1
        for idx in range(H):
            c = Ss[idx][w]
            if c == '#':
                for x in range(last_idx, idx):
                    lenVer[x][w] = buf
                buf = 0
                last_idx = idx+1
            else:
                buf += 1
    ans = 0
    for h in range(H):
        for w in range(W):
            ans = max(ans, max(lenVer[h][w]-1,0)+max(lenHor[h][w]-1,0)+1)
    return ans

print(main())
