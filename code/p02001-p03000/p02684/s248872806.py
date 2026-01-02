#import sys
MOD = 10 ** 9 + 7
INFI = 10**10
#input = sys.stdin.readline
import math

import itertools
import heapq
#import bisect

import copy
from functools import lru_cache

def sosuhante(n):
    for k in range(2, int(math.sqrt(n))+1):
        if n% k ==0:
            return False
    return True
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

def kingaku(a,b,n):
    keta=len(str(n))
    return a*n+b*keta

def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default

#    h,w,a,b = map(int, input().split())
#    c = [[0 for j in range(n)] for i in range(n)]

def ret(a):
    c=[None]*(len(a)-1)
    if len(a)==1:
        return a[0]
    elif len(a)==0:
        return 0
    for i in range(1,len(a)):
        c[i-1]=abs(a[i]-a[i-1])
    return ret(c)


def main():
    n,k=map(int,input().split())
    a =list(map(int,input().split()))
    town=[-1 for _ in range(n)]
    town[0]=0
    now=0
    for i in range(n):
        if town[a[now]-1]==-1:
            town[a[now]-1]=i+1
            now=a[now]-1
        else:
            sec=a[now]-1
            break
#        if i==n-1:
  #          sec=a[now]-1
    town2 = [-1 for _ in range(n)]
    town2[sec] = 0
    now = sec
    for i in range(n):
        if town2[a[now] - 1] == -1:
            town2[a[now] - 1] = i + 1
            now = a[now] - 1
        else:
            thi = a[now] - 1
            break
#    print(town)
#    print(town2)
    firstloop=max(town)+1
    secondloop=max(town2)+1
    ans=0
    if k<firstloop:
        ans=town.index(k)+1
    else:
        k-=firstloop
        kai=k//secondloop
        k-=kai*secondloop
        ans=town2.index(k)+1
    print(ans)

if __name__ == "__main__":

    main()