#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=tf-8
#

"""
"""

from collections import defaultdict
from itertools import accumulate
import bisect

import sys
input = sys.stdin.readline
import math as mt

MAXN = 10**6 +1
  
# stores smallest prime factor for 
# every number 
spf = [0 for i in range(MAXN)] 
  
# Calculating SPF (Smallest Prime Factor)  
# for every number till MAXN. 
# Time Complexity : O(nloglogn) 
def sieve(): 
    spf[1] = 1
    for i in range(2, MAXN): 
          
        # marking smallest prime factor  
        # for every number to be itself. 
        spf[i] = i 
  
    # separately marking spf for  
    # every even number as 2 
    for i in range(4, MAXN, 2): 
        spf[i] = 2
  
    for i in range(3, mt.ceil(mt.sqrt(MAXN))): 
          
        # checking if i is prime 
        if (spf[i] == i): 
              
            # marking SPF for all numbers 
            # divisible by i 
            for j in range(i * i, MAXN, i):  
                  
                # marking spf[j] if it is  
                # not previously marked 
                if (spf[j] == j): 
                    spf[j] = i 


def getFactorization(x): 
    ret = set([]) 
    while (x != 1): 
        ret.add(spf[x]) 
        x = x // spf[x] 
  
    return ret 


def solve(n,a):
    sieve()
    gcd_primes = getFactorization(a[0])
    seen_primes = set([])
    flag_pcp = True
    for aa in a:
        ps = getFactorization(aa)
        if flag_pcp:
            if not (seen_primes & ps):
                seen_primes |= ps
            else:
                flag_pcp = False
        gcd_primes &= ps
    if flag_pcp:
        print('pairwise coprime')
    elif gcd_primes:
        print('not coprime')
    else:
        print('setwise coprime')





            


            

def main():
    n = int(input())
    a = list(map(int,input().split()))
    solve(n,a)


if __name__ == "__main__":
    main()