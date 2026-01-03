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
    yakusuu = make_divisors(N)
    
    ans = INF
    for i,val in enumerate(yakusuu):
        for j,vol in enumerate(yakusuu):
            if val*vol == N:
                tmp = max(val,vol)
                tmptmp = len(str(tmp))
                
                if ans > tmptmp:
                    ans = tmptmp
                    
    print(ans)
    
    
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
                
    # divisors.sort()
    return divisors
    
if __name__ == "__main__":
	main()
