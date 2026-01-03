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
    for i in range(N):
        a,b = inputMap()
        ab.append((a,b))
        
    cd = []
    for i in range(M):
        c,d = inputMap()
        cd.append((c,d))
        
    man = []
    for i,val in enumerate(ab):
        a,b = val
        tmp = []
        for j,vol in enumerate(cd):
            c,d = vol
            tmp.append(abs(a-c)+abs(b-d))
        
        tmptmp = 0
        ind = 0
        for k, v in enumerate(tmp):
            if k == 0:
                tmptmp = v
            else:
                if tmptmp > v:
                    tmptmp = v
                    ind = k
        print(ind+1)
        
        
    
if __name__ == "__main__":
	main()
