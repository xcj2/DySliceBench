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
    
    ma = 0
    e = [[] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if(S[i][j] == '1'): e[i].append(j) 
    for i in range(N):
        dep = [-1] * N
        q = collections.deque()
        dep[i] = 0
        q.append(i)
        while(len(q) > 0):
            now = q.popleft()
            for nxt in e[now]:
                if dep[nxt] == -1:
                    dep[nxt] = dep[now] + 1
                    q.append(nxt)
        for j in range(N):
            ma = max(ma, dep[j])
    
    print(ma + 1)
        

if __name__ == "__main__":
    main()
