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
import random
 
# NO, PAY-PAY
#import numpy as np
#import statistics
#from statistics import mean, median,variance,stdev
 
def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))
 
def main():
    N = inputInt()
    s = []
    flg = False
    onry = False
    tmp_max = 0
    tmp_arr = []
    for i in range(N):
        tmp = inputInt()
        s.append(tmp)
        if tmp % 10 != 0:
            tmp_max += tmp
            tmp_arr.append(tmp)
            flg = True
            if onry == False:
                onry = True
            else:
                onry = None
            
    if flg == False:
        print(0)
        sys.exit()
        
    if onry == True or tmp_max % 10 != 0:
        print(sum(s))
        sys.exit()
        
    print(sum(s)-min(tmp_arr))
        
        
if __name__ == "__main__":
	main()
