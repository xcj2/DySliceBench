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
    
    b = [0 for _ in range(N)]
    base = (N//2)
    cnt = 1
    
    flg = False
    if N % 2 == 0:
        flg = True
    
    for i, val in enumerate(A):
        
        if flg == True:
            if i == 0:
                b[base] = val
            elif i % 2 == 1:
                b[base-cnt] = val
            else:
                b[base+cnt] = val
                cnt+=1
        else:
            if i == 0:
                b[base] = val
            elif i % 2 == 1:
                b[base+cnt] = val
            else:
                b[base-cnt] = val
                cnt+=1
    
    print(*b)
    
        
if __name__ == "__main__":
	main()
