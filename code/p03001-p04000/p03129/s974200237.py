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

import os
 
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
    
    ans = 0
    for i in range(1, N+1):
        if i % 2 == 1:
            ans += 1
            if ans >= K:
                print("YES")
                sys.exit()
                
    print("NO")
    
    
if __name__ == "__main__":
	main()
