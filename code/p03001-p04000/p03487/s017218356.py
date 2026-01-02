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
    a = inputList()
    
    tmp = {}
    for i in a:
        if i in tmp:
            tmp[i] += 1
        else:
            tmp[i] = 1
            
    ans = 0
    for k, v in tmp.items():
        if k != v:
            if k < v:
                ans += v-k
            else:
                ans += v
    
    print(ans)
            	
if __name__ == "__main__":
	main()
