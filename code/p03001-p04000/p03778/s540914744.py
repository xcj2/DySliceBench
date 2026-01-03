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
    W,a,b = inputMap()
    tmp1 = abs((a+W) - b)
    tmp2 = abs(a-(b+W))
    
    if b <= (a+W) and b >= a:
        print(0)
        sys.exit()
    if b+W <= (a+W) and b+W >= a:
        print(0)
        sys.exit()
    print(min(tmp1,tmp2))
    
    
if __name__ == "__main__":
	main()
