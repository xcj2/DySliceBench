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
    N = inputInt()
    A = inputList()
    B = inputList()
    C = inputList()
    
    ans = 0
    old = -1
    for i, val in enumerate(A):
        if old != -1 and old+1 == val:
            ans += C[old-1]
        ans += B[val-1]
        old = val
            
    print(ans)
    
if __name__ == "__main__":
	main()
