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
    ans = {}
    for _ in range(N):
        tmp = inputInt()
        if tmp in ans:
            ans[tmp] += 1
        else:
            ans[tmp] = 1
        
    o = 0
    for v in ans.values():
        if v % 2 == 1:
            o += 1
    print(o)
        
            	
if __name__ == "__main__":
	main()
