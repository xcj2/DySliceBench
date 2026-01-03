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
    N,K = inputMap()
    ab = []
    
    for _ in range(N):
        a,b = inputMap()
        ab.append((a,b))
        
    ab.sort()
    tmp = K
    
    for i, val in enumerate(ab):
        a,b = val
        tmp -= b
        if tmp <= 0:
            print(a)
            sys.exit()
    
if __name__ == "__main__":
	main()
