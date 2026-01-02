# -*- coding: utf-8 -*-
import sys
import copy
import collections
from bisect import bisect_left
from bisect import bisect_right
from collections import defaultdict
from heapq import heappop, heappush
import math

# NO, PAY-PAY
#import numpy as np
#import statistics
#from statistics import mean, median,variance,stdev

def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))
 
def main():
    N = inputInt()
    K = inputInt()
    
    ans = 1
    for _ in range(N):
        if ans <= K:
            ans = ans * 2
        else:
            ans += K
    
    print(ans)
    
            	
if __name__ == "__main__":
	main()
