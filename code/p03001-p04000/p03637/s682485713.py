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
    
    tmp = 0
    gu = 0
    for i, val in enumerate(a):
        if val % 4 == 0:
            tmp += 1
            continue
        if val % 2 == 0:
            gu += 1
            
    if tmp >= N // 2:
        print("Yes")
        sys.exit()
    
    aaa = (N // 2) - tmp
    gugu = gu // 2
    #print("{} {}".format(aaa, gu))
    if aaa <= gugu:
        print("Yes")
        sys.exit()
        
    print("No")
    
    
if __name__ == "__main__":
	main()
