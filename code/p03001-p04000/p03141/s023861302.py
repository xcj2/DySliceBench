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
    N = inputInt()
    A = []
    B = []
    sai = []
    sai2 = []
    for i in range(N):
        a,b = inputMap()
        A.append(a)
        B.append(b)
        sai.append(a+b)
        sai2.append((a+b, i))
        
    sai2.sort()
    sai2 = sai2[::-1]
    
    takahashi = 0
    aoki = 0
    for i,val in enumerate(sai2):
        val, no = val
        if i == 0:
            takahashi += A[no]
        else:
            if i % 2 == 1:
                aoki += B[no]
            else:
                takahashi += A[no]
            
    print(takahashi - aoki)
                
    
if __name__ == "__main__":
	main()
