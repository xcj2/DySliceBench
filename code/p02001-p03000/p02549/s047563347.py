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

def soinsubunkai_e(n,m): #高速素因数分解 m[n]=nを割ることの出来る最小の素数
    a = set()
    i = 1
    while n>1:
        a.add(m[n])
        n=n//m[n]
    nokori=n
    a.add(nokori)
    return a

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


def era(n): #b[n]=nを割ることの出来る最小の素数　の配列を生成　エラトステネスの篩
    b=[i for i in range(n+1)]
    for i in range(2,int(math.sqrt(n)+10)):
        j=1
        temp=i*j
        while temp<=n:
            b[temp]=min(i,b[temp])
            temp+=i
    return b


def main():
    #l,r,d=map(int,input().split())
    MODT=998244353
    n,k=map(int,input().split())
    step=[]
    for i in range(k):
        l,r=map(int,input().split())
        step.append([l,r])
    dp=[0 for i in range(n*2+2)]
    dp[1]=1
    dp[2]=-1
#    print(step)
    for i in range(1,n+1):
  #      print(dp)
        dp[i]+=dp[i-1]
        dp[i]%=MODT
        for j in range(k):
            dp[i+step[j][0]]+=dp[i]%MODT
            dp[i+step[j][1]+1]-=dp[i]%MODT
 #   print(dp)
  #  print(dp)
    print(dp[n]%MODT)






if __name__ == "__main__":

    main()
