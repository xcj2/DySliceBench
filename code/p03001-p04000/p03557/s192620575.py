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
    N = inputInt()
    A = inputList()
    B = inputList()
    C = inputList()
    
    A.sort()
    B.sort()
    C.sort()
    
    tmplist = []
    for i,val in enumerate(B):
        target1 = bisect_left(C, val+1)
        tmp = N - target1
        tmplist.append(tmp)
            
    for i in range(N-2, -1, -1):
        tmplist[i] = tmplist[i] + tmplist[i+1]
        
    #print(tmplist)
    
    ans = 0
    for i,val in enumerate(A):
        target1 = bisect_left(B, val+1)
        if target1 == N:
            continue
        ans += tmplist[target1]
        
    print(ans)
    
    
            	
if __name__ == "__main__":
	main()
