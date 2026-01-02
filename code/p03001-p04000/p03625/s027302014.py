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
    
    tmp = {}
    for i, val in enumerate(A):
        if val in tmp:
            tmp[val] += 1
        else:
            tmp[val] = 1
            
    ans = []
    for k, v in tmp.items():
        if v >= 4:
            ans.append(k)
            ans.append(k)
        elif v >= 2:
            ans.append(k)
            
    if len(ans) == 0:
        print(0)
        sys.exit()
    ans.sort()
    print(ans[-1] * ans[-2])
    
    
if __name__ == "__main__":
	main()
