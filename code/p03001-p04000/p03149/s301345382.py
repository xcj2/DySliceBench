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
    N1,N2,N3,N4 = inputMap()
    inp = []
    inp.append(N1)
    inp.append(N2)
    inp.append(N3)
    inp.append(N4)
    flgs = [False, False, False, False]
    
    if 1 in inp:
        flgs[0] = True
    else:
        print("NO")
        sys.exit()
        
    if 7 in inp:
        flgs[1] = True
    else:
        print("NO")
        sys.exit()
        
    if 9 in inp:
        flgs[2] = True
    else:
        print("NO")
        sys.exit()
        
    if 4 in inp:
        flgs[3] = True
    else:
        print("NO")
        sys.exit()
    
    for i in flgs:
        if i == False:
            print("NO")
            ys.exit()
            
    print("YES")
    
if __name__ == "__main__":
	main()
