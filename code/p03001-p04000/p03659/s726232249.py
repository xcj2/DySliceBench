# -*- coding: utf-8 -*-
import sys
import copy
import collections
from bisect import bisect_left
from bisect import bisect_right
from collections import defaultdict
from heapq import heappop, heappush
import math
import itertools
 
# NO, PAY-PAY
#import numpy as np
#import statistics
#from statistics import mean, median,variance,stdev
 
def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))
 
def main():
    N = inputInt()
    A = inputList()
    
    ans = float("inf")
    
    if N == 2:
        print(abs(A[0] - A[1]))
        sys.exit()
    
    a_sp = []
    for i, val in enumerate(A):
        if i == 0:
            a_sp.append(val)
            continue
        tmp = val + a_sp[i-1]
        a_sp.append(tmp)
        
    for i, val in enumerate(a_sp):
        if i == (len(a_sp)-1):
            break
            
        tmp = abs(val - ((a_sp[-1])-val))
        
        if tmp < ans:
            ans = tmp
            
    print(ans)
        
if __name__ == "__main__":
	main()
