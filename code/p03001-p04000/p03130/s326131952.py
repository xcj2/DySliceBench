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
    a1, b1 = inputMap()
    a2, b2 = inputMap()
    a3, b3 = inputMap()
    
    maps = {}
    maps[a1] = 1
    maps[b1] = 1
    
    if a2 in maps:
        maps[a2] += 1
    else:
        maps[a2] = 1
        
    if b2 in maps:
        maps[b2] += 1
    else:
        maps[b2] = 1
        
    if a3 in maps:
        maps[a3] += 1
    else:
        maps[a3] = 1
        
    if b3 in maps:
        maps[b3] += 1
    else:
        maps[b3] = 1
        
    for k,v in maps.items():
        if v > 2:
            print("NO")
            sys.exit()
            
    print("YES")
    
    
if __name__ == "__main__":
	main()
