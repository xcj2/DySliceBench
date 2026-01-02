#import sys
MOD = 10 ** 9 + 7
INFI = 10**10
#input = sys.stdin.readline
import math
from collections import deque
import itertools
import heapq
#import bisect
from fractions import Fraction
import copy
from functools import lru_cache
from collections import defaultdict
import pprint

#oo=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# ko=list("abcdefghijklmnopqrstuvwxyz")

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

def soinsubunkai(n):
    a = []
    i = 1
    while i*i <= n:
        if n % i == 0 and i!=1:
            a.append(i)
            n=n//i

        if n% i !=0 or i==1:
            i += 1
    nokori=[n]
    return a + nokori


def main():
    n,m,k=map(int,input().split())
    aa=list(map(int,input().split()))
    bb=list(map(int,input().split()))
    a=[0]
    a.extend(aa)
    b=[0]
    b.extend(bb)
    maxcount=0
    totaltime=0
    maxa=0
    maxb=0
    for i in range(n+1):
        if totaltime+a[i]<=k:
            totaltime+=a[i]

        else:
            maxa=i-1
            break
        maxa = i
    totaltime=0
    maxb=0
    nowatotal=sum(a[0:maxa+1])
    nowbtotal=sum(b[0:maxb+1])
    for i in range(maxa,-1,-1):
#        nowbtotal = sum(b[0:maxb + 1])
        for j in range(maxb,m+1):
            nowcount=i+j
            if nowatotal+nowbtotal+b[j]<=k:
                maxcount=max(maxcount,nowcount)
                maxb+=1
            else:
                break
            nowbtotal+=b[j]
        nowatotal-=a[i]
    print(maxcount)

if __name__ == "__main__":

    main()