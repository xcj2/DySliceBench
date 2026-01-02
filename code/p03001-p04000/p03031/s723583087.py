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

def main():
    N,M = ints_raw()
    SS =[0]*(N+1)
    for midx in range(M):
        ks = ints_raw()
        for j in ks[1:]:
            SS[j-1] += 1<<midx
    p = 0
    pis = ints_raw()
    for midx in range(M):
        pi = pis[midx]
        if pi>=2:
            return 0
        if pi ==1:
            p+=1<<midx
    ans = 0
    for dbit in range(2**N):
        tmp = 0
        for j in range(N):
            if (dbit & (1<<j)):
                tmp = tmp^SS[j]
        if tmp == p:
            ans+=1
    return ans

print(main())
