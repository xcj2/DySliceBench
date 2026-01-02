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
    M,D = inputMap()
    ans = 0
    
    for i in range(2,M+1):
        for j in range(10,D+1):
            tmp = str(j)
            
            d1 = int(tmp[1])
            d10 = int(tmp[0])
            
            if d1 >= 2 and d10 >= 2 and d1 * d10 == i:
                #print("{}月 {} {}".format(i,d10,d1))
                ans += 1
                
    print(ans)
    
    
    
if __name__ == "__main__":
	main()
