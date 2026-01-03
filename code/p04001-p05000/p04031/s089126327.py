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
    a = inputList()
    
    flg = True
    for i,vol in enumerate(a):
        if i == 0:
            continue
        if vol != a[i-1]:
            flg = False
            break
            
    if flg == True:
        print(0)
        sys.exit()
    
    ans = INF
    for i in range(-100,101):
        cst = 0
        for j,vol in enumerate(a):
            cst += (vol-i)**2
            
        if ans > cst:
            ans = cst
            #print("{} {}".format(cst,ans))
            
    print(ans)
    
if __name__ == "__main__":
	main()
