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
    a = inputList()
    ans = {}
    
    for i, val in enumerate(a):
        if val in ans:
            ans[val] += 1
        else:
            ans[val] = 1
            
        if val+1 in ans:
            ans[val+1] += 1
        else:
            ans[val+1] = 1
            
        if val-1 in ans:
            ans[val-1] += 1
        else:
            ans[val-1] = 1
            
    tmp = 0
    for i in ans.values():
        if tmp < i:
            tmp = i
            
    print(tmp)
    
    
if __name__ == "__main__":
	main()
