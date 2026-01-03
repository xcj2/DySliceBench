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
    A,B,C = inputMap()
    
    tot = A+B+C
    tmp = tot - 7
    if max(A,B,C) == 7 and min(A,B,C) == 5 and tmp == 10:
        print("YES")
    else:
        print("NO")
    
if __name__ == "__main__":
	main()
