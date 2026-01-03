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
    
    if N == 1:
        print(1)
        sys.exit()
    
    ans = 0
    ansans = 0
    for i in range(1, N+1):
        tmp = 0
        han = i
        aaa = i
        while True:
            if han % 2 == 0:
                han = han / 2
                tmp += 1
            else:
                break
        if tmp > ans:
            ans = tmp
            ansans = aaa
            
    print(ansans)
    
if __name__ == "__main__":
	main()
