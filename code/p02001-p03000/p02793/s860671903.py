#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7
def main():
    n=I()
    lis=LI()
    def prime_factorize(n):
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return a
    lists=[Counter(prime_factorize(lis[i])) for i in range(n)]
    C=Counter([])
    for i in range(n):
        x=lists[i]
        for j in x.keys():
            C[j]=max(C[j],x[j])
    #print(C)
    
    ans=1
    '''for i in range(n):
        x=lists[i]
        y=1
        for j in C.keys():
            y=(y*pow(j,C[j]-x[j],mod))%mod
        #print(y%mod)
        ans=(ans+y)%mod
    print(ans%mod)'''
    invmod=0
    for i in range(n):
        invmod=(invmod+pow(lis[i]%mod,mod-2,mod))%mod
    for x in C.keys():
        ans=(ans*pow(x,C[x],mod))%mod
    print(ans*invmod%mod)
        
if __name__=="__main__":
    main()
        
        
    
    
        
    
    
