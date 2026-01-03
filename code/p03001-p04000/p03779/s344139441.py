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
    X = inputInt()
    
    ans = 0
    total = 0
    for i in range(1,X+1):
        total += i
        if total >= X:
            ans = i
            break
            
    print(ans)
    
    
if __name__ == "__main__":
	main()
