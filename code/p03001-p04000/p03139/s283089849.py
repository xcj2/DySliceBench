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
    N,A,B = inputMap()
    
    ans1 = min(A,B)
    tmp = N-A
    if tmp >= B:
        ans2 = 0
    else:
        ans2 = B-tmp
        
    print("{} {}".format(ans1, ans2))
    
    
if __name__ == "__main__":
	main()
