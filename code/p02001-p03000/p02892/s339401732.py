from sys import stdin
import sys
#import numpy as np
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
def main():
    N = ri()
    S = [""] * N
    for i in range(N): S[i] = rs()

    bw = [-1] * N
    q = collections.deque()
    bw[0] = 0
    q.append(0)
    while(len(q) > 0):
        now = q.popleft()
        for nxt in range(N):
            if S[now][nxt] == '0': continue
            if bw[nxt] == -1:
                bw[nxt] = bw[now] ^ 1
                q.append(nxt)
            elif bw[nxt] == bw[now]:
                print(-1)
                sys.exit(0)
    
    inf = int(1e9)
    wf = [[inf] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            wf[i][j] = 1 if S[i][j] == '1' else inf
            if i == j: wf[i][j] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                wf[i][j] = min(wf[i][j], wf[i][k] + wf[k][j])
    
    ma = 0
    for i in range(N):
        for j in range(N):
            ma = max(ma, wf[i][j])

    print(ma + 1)

if __name__ == "__main__":
    main()
