import bisect, copy, heapq, math, sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
def celi(a,b):
    return -(-a//b)
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

def main():
    r,c,k=map(int,input().split())
    rcv=[list(map(int,input().split())) for i in range(k)]

    dpn=[[0]*4 for i in range(c+1)]

    dic={}
    for i in range(k):
        r1,c1,v=rcv[i]
        dic[(r1,c1)]=v

    for i in range(r):
        for j in range(c):
            dpn[j+1][0]=max(dpn[j+1][0],max(dpn[j+1]))
            if (i+1,j+1) in dic:
                for k in range(3)[::-1]:
                    dpn[j+1][k+1]=max(dpn[j+1][k]+dic[(i+1,j+1)],dpn[j][k]+dic[(i+1,j+1)])
            for k in range(4):
                dpn[j+1][k]=max(dpn[j+1][k],dpn[j][k])
        # print(dpn)
    print(max(dpn[-1]))

main()