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
    ans = 1
    
    for i in range(N,0,-1):
        tmp = math.sqrt(i)
        if tmp.is_integer():
            print(i)
            sys.exit()
            	
if __name__ == "__main__":
	main()
