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
    N = inputInt()
    A = inputList()
    
    free = 0
    a = [0 for _ in range(8)]
    
    for i in A:
        if i < 400:
            a[0] += 1
        elif i < 800:
            a[1] += 1
        elif i < 1200:
            a[2] += 1
        elif i < 1600:
            a[3] += 1
        elif i < 2000:
            a[4] += 1
        elif i < 2400:
            a[5] += 1
        elif i < 2800:
            a[6] += 1
        elif i < 3200:
            a[7] += 1
        else:
            free += 1
            
    ans = 0
    for i in a:
        if i == 0:
            continue
        if i != 0:
            ans += 1
            
    if ans != 0:
        print("{} {}".format(ans, ans+free))
    else:
        print("{} {}".format(1, ans+free))
    
        
if __name__ == "__main__":
	main()
