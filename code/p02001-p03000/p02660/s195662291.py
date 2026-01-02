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

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0 and i!=1:
            lower_divisors.append(i)
            n=n//i
  #          if i != n // i:
  #              upper_divisors.append(n//i)
        if n% i !=0 or i==1:
            i += 1
    nokori=[n]
    return lower_divisors + nokori # upper_divisors[::-1]

def main():
    n=int(input())
 #   n=2**40
    yaku=make_divisors(n)
    memo = defaultdict(int)
    for i in range(len(yaku)):
        memo[yaku[i]]+=1
    ans=0
    for b in memo.values():
        if b<=2:
            ans+=1
        elif b>=3 and b<=5:
            ans+=2
        elif b>=6 and b<=9:
            ans+=3
        elif b >= 10 and b <= 14:
            ans += 4
        elif b >= 15 and b <= 20:
            ans += 5
        elif b >= 21 and b <= 27:
            ans += 6
        elif b >= 28 and b <= 35:
            ans += 7
        elif b >= 36 and b <= 44:
            ans += 8
        elif b>=45:
            ans+=9


    if n==1:
        print(0)
    else:
        print(ans)


 #   print(memo)
 #   print(yaku)








if __name__ == "__main__":

    main()