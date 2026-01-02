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
    N = inputInt()
    H = inputInt()
    W = inputInt()
    
    ans = 0
    if N == H:
        if N == W:
            print(1)
        else:
            print(N-W+1)
    else:
        if N == W:
            print(N-H+1)
        else:
            print((N-H+1) * (N-W+1))
                
    
if __name__ == "__main__":
	main()
