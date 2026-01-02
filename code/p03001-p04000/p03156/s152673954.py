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
    A,B = inputMap()
    P = inputList()
    
    rinko = []
    manaka = []
    nene = []
    for i in P:
        if i <= A:
            rinko.append(i)
        elif i >= B+1:
            nene.append(i)
        else:
            manaka.append(i)
            
    print(min(len(rinko), len(nene), len(manaka)))
    
if __name__ == "__main__":
	main()
