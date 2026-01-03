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
    T = inputList()
    
    M = inputInt()
    px = []
    for i in range(M):
        p,x = inputMap()
        px.append((p,x))
        
    ans = []
    for i,val in enumerate(px):
        tmp = 0
        p,x = val
        for j,vol in enumerate(T):
            if j == p-1:
                tmp += x
            else:
                tmp += vol
        ans.append(tmp)
        
    for i in ans:
        print(i)
    
if __name__ == "__main__":
	main()
