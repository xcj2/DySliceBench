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
    K,A,B = inputMap()
    
    if A+2 >= B:
        print(1+K)
        sys.exit()
        
    sai = A+1
    ans = 1
    if K < sai:
        print(1+K)
        sys.exit()
        
    else:
        sai = A-1
        K = K-sai
        
        if K % 2 == 1:
            K -= 1
            ans = 1
            kai = int(K / 2)
            ans += (B-A)*kai
            ans += A
            
        else:
            kai = int(K / 2)
            ans = (B-A)*kai
            ans += A
        
    print(ans)
    #print(48518828981938099)
    
    
if __name__ == "__main__":
	main()
