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
 
# NO, PAY-PAY
#import numpy as np
#import statistics
#from statistics import mean, median,variance,stdev
 
def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))
 
def main():
    r,g,b = inputMap()
    
    tmp = str(r) + str(g) + str(b)
    tmp1 = int(tmp)
    
    if tmp1 % 4 == 0:
        print("YES")
    else:
        print("NO")
    
        
if __name__ == "__main__":
	main()
