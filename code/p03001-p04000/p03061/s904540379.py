from heapq import heappush,heappop
import queue
import re
import math
import functools
import numpy

def int_raw():
    return int(input())

def ss_raw():
    return input().split()

def ints_raw():
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


N = int_raw()
As = ints_raw()


def main():
    f_gcds = [As[0]]
    for i in range(1,N):
        f_gcds.append(gcd(As[i],f_gcds[-1]))
    b_gcds = [0]*(N-1)+[As[-1]]
    for i in range(N-2,-1,-1):
        b_gcds[i] = gcd(As[i],b_gcds[i+1])
    ans = max(b_gcds[1],f_gcds[-2])
    for i in range(1,N-1):
        ans = max(ans,gcd(f_gcds[i-1],b_gcds[i+1]))
    return ans

print(main())
