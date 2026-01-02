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

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def main():
    h,w,k2=map(int,input().split())
    c=[]
    for i in range(h):
        temp=list(input())
        c.append(temp)

    for i in range(h):
        for j in range(w):
            if c[i][j]==".":
                c[i][j]=0
            else:
                c[i][j]=1
#    print(c)
    count=0
    orig=copy.deepcopy(c)
    for i in itertools.product(range(2),repeat=h):
        for j in itertools.product(range(2), repeat=w):
            c=copy.deepcopy(orig)
            for l in range(h):
                for k in range(w):
                    if i[l]==1:
                        c[l][k]=0
                    if j[k]==1:
                        c[l][k]=0
            temp=0
            for l in range(h):
                temp+=sum(c[l])
            if temp==k2:
                count+=1
    print(count)


if __name__ == "__main__":

    main()