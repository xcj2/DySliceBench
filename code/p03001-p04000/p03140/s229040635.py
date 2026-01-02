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
    A = input()
    B = input()
    C = input()
    
    ans = 0
    for i in range(N):
        if A[i] == B[i] and A[i] == C[i]:
            pass
        else:
            if A[i] != B[i] and A[i] != C[i] and B[i] != C[i]:
                ans += 2
            else:
                ans += 1
                
    print(ans)
                
    
if __name__ == "__main__":
	main()
