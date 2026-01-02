from heapq import heappush, heappop
from collections import deque
import re
import math
import functools

def sRaw():
    return input().rstrip("\r")

def iRaw():
    return int(input())


def ssRaw():
    return input().split()


def isRaw():
    return list(map(int, ssRaw()))

INF = 1 << 29


def make1d_arr(n, val=INF):
    return [val for i in range(n)]


def make2d_arr(h, w, val=INF):
    return [[val for i in range(w)]for i in range(h)]


def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b)


def BFord(n,es):
    v_cost = [INF]*n
    v_cost[0] = 0
    for v in range(n*2):
        for e in es:
            frm = e[0]
            to = e[1]
            if v_cost[to] > v_cost[frm]+e[2]:
                v_cost[to] = v_cost[frm]+e[2]
                if v >= n:
                    v_cost[to] = -INF
        if v == n-1:
            prev = v_cost[:]
    v_cost = [-INF if prev[idx]!=v_cost[idx] else v_cost[idx] for idx in range(n)]
    return v_cost
    
def ZAlgo(s):
    l = len(s)
    A = [0]*l
    i =1
    j =0
    A[0]=l
    while i<l:
        while i+j<l and s[j] == s[i+j]:
            j+=1
        if j==0:
            i+=1
            continue
        A[i]=j
        k=1
        while (i+k<l) and (k+A[k]<j):
            A[i+k] =A[k]
            k+=1
        i+=k
        j-=k
    return A


DIV = 998244353

def main():
    N = iRaw()
    As = isRaw()
    Bs = isRaw()
    BAs = list(zip(Bs,As))
    BAs.sort()
    AIs = [[ba[1],idx] for idx,ba in enumerate(BAs)]
    AIs.sort()
    sAidx = [0]*len(AIs)
    for sIdx,ai in enumerate(AIs):
        a,idx = ai
        if a>BAs[sIdx][0]:
            return "No"
        sAidx[idx]=sIdx
    cycleSize = 0
    curIdx = 0
    visited = [0]*len(AIs)
    while visited[curIdx]==0:
        visited[curIdx]=1
        cycleSize +=1
        curIdx = sAidx[curIdx]
    if cycleSize < N:
        return "Yes"

    for idx in range(N-1):
        if AIs[idx+1][0]<=BAs[idx][0]:
            return "Yes"
    return "No"

if __name__ == "__main__":
    print(main())
