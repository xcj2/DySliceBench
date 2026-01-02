# -*- coding: utf-8 -*-
import sys
import copy
import collections
from bisect import bisect_left
from bisect import bisect_right
from collections import defaultdict
from heapq import heappop, heappush, heapify
import math
import itertools
import random
 
# NO, PAY-PAY
#import numpy as np
#import statistics
#from statistics import mean, median,variance,stdev
 
INF = float('inf')
def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))
 
def main():
    N = inputInt()
    
    if is_prime(N):
        print(N-1)
        sys.exit()
        
    ll = factorize(N)
    ll.sort()
    
    if len(ll) == 2:
        a = ll[0] -1
        b = ll[1] -1
        print(a + b)
        sys.exit()
        
    tmp = math.sqrt(N)
    max = (tmp // 1) + 1
    ans = INF
    for i in range(1, int(max)):
        b = N / i
        if b.is_integer():
            tmp = (i-1) + (b-1)
            if ans > tmp:
                ans = tmp
                
    print(int(ans))
    
def is_prime(n): 
    i = 2
    while i * i <=n:
        if n % i == 0:
            return False
        i += 1
    return True
    
def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct
    
if __name__ == "__main__":
	main()
