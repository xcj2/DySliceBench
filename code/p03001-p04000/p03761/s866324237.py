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
    S = []
    boxx = []
    for i in range(N):
        tmp = list(input())
        if i == 0:
            boxx.append(tmp)
        else:
            momo = []
            for c in tmp:
                if c in boxx[-1]:
                    momo.append(c)
                    boxx[-1].remove(c)
            boxx.append(momo)
            
    ans = boxx[-1]
    ans.sort()
    print("".join(ans))
    
    
if __name__ == "__main__":
	main()
