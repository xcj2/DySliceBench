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
    p = inputList()
    
    tmp = 0
    tona = 0
    flg = False
    for i, val in enumerate(p):
        if i+1 == val:
            tmp += 1
            if flg == True:
                tona += 1
                flg = False
            else:
                flg = True
        else:
            flg = False
            
    print(tmp-tona)
    
    
if __name__ == "__main__":
	main()
