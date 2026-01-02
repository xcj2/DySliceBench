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


def main():
    N = iRaw()
    ans =0
    if N%2!=0:
        return N//2
    else:
        return (N-1)//2

if __name__ == "__main__":
    print(main())
