# -*- coding: utf-8 -*-
import sys
import copy
import collections
from bisect import bisect_left
from bisect import bisect_right
from collections import defaultdict
from heapq import heappop, heappush
import math

# NO, PAY-PAY
#import numpy as np
#import statistics
#from statistics import mean, median,variance,stdev

def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))
 
def main():
    N,Z,W = inputMap()
    A = inputList()
    
    if N ==1:
        print(abs(A[-1]-W))
    else:
        print(max(abs(A[-1]-W), abs(A[-2]-A[-1])))
    
    '''
    A_max = max(A)
    A_min = min(A)
    
    ans = 0
    tmp1 = abs(Z - A[-1])
    tmp2 = abs(A[-1] - W)
    tmp3 = abs(A_max - A[-1])
    tmp4 = abs(A[-1] - A_min)
    
    tmp5 = 0
    if A_max == A[-1] or A_min == A[-1]:
        tmp5 = abs(A_max - A_min)
    
    print(max(tmp1, tmp2, tmp3, tmp4, tmp5))
    '''
            	
if __name__ == "__main__":
	main()
