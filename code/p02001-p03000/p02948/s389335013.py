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
    N,M = inputMap()
    ab = []
    heapify(ab)
    for i in range(N):
        a,b = inputMap()
        if a > M:
            continue
        heappush(ab, (a,b))
    
    ans = 0
    pq = []
    heapify(pq)
    for i in range(1,M+1):
        while True:
            if len(ab) == 0 or ab[0][0] != i:
                break
            a,b = heappop(ab)
            heappush(pq, -b)
            
        if len(pq) > 0:
            ans = ans + (heappop(pq) * (-1))
        
    
    print(ans)
    
if __name__ == "__main__":
	main()
