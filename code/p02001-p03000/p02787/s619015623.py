from heapq import heappush,heappop
import queue
import re
import math
import functools


def i_raw():
    return int(input())

def ss_raw():
    return input().split()

def is_raw():
    return list(map(int, ss_raw()))

INF = 1<<29

def make1d_arr(n,val=INF):
    return [val for i in range(n)]

def make2d_arr(h,w,val =INF):
    return [[val for i in range(w)]for i in range(h)]

def gcd (a,b):
    if(b==0):
        return a
    return gcd(b,a%b)


def main():
    H,N = is_raw()
    ABs = [is_raw() for _ in range(N)]
    MA = max([ab[0] for ab in ABs])
    dp = [INF]*(H+MA+1)
    dp[0]=0
    for h in range(1,len(dp)):
        for ab in ABs:
            a,b = ab
            if h < a:
                continue
            dp[h] = min(dp[h],b+dp[h-a])
    return min([dp[h] for h in range(H,len(dp))])


print(main())
