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
    k=int(input())
    keta1=[x for x in range(1,10)]
    oriketa=copy.deepcopy(keta1)
    def next(keta,newketa):
        for i in range(len(keta)):
            plus=keta[i]%10+1
            eq=keta[i]%10
            minus=keta[i]%10-1
            if plus<=9:
                newketa.append(keta[i]*10+plus)
            newketa.append(keta[i]*10+eq)
            if minus>=0:
                newketa.append(keta[i]*10+minus)
        return
    ketan=[[] for i in range(10)]
    next(keta1,ketan[0])
    ketan[0]=sorted(ketan[0])
    oriketa.extend(ketan[0])
    for i in range(9):
        next(ketan[i],ketan[i+1])
        ketan[i+1] = sorted(ketan[i+1])
        oriketa.extend(ketan[i+1])

    #print(oriketa)
    print(oriketa[k-1])



if __name__ == "__main__":

    main()