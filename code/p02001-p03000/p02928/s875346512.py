# -*- coding: utf-8 -*-
import sys
import copy
import collections
from bisect import bisect_left
from bisect import bisect_right
from collections import defaultdict
from heapq import heappop, heappush, heapify
import math
import itertools
import random
 
# NO, PAY-PAY
#import numpy as np
#import statistics
#from statistics import mean, median,variance,stdev
 
INF = float('inf')
def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))
 
def main():
    N,K = inputMap()
    A = inputList()
    
    ten = 0
    ten_zen = 0
    for i,vol in enumerate(A):
        for j,val in enumerate(A):
            if i >= j:
                if vol > val:
                    #print("{} {}".format(vol, val))
                    ten_zen += 1
                continue
            if vol > val:
                ten += 1
                ten_zen += 1
                
    #ans = (K*ten) + ((K-1)*ten_zen)
    #ans = ans%1000000007
    
    ans = (K*ten)%1000000007
    tmp = (K*(K-1)) // 2
    ans = ans + ((tmp * ten_zen)%1000000007)
    
    print(ans%1000000007)
    
    
if __name__ == "__main__":
	main()
