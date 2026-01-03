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
    N,L = inputMap()
    S = []
    for _ in range(N):
        tmp = input()
        S.append(tmp)
        
    S.sort()
    ans = ""
    for vol in S:
        ans += vol
        
    print(ans)
    
if __name__ == "__main__":
	main()
