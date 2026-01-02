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
    N,K = inputMap()
    A = inputList()
    
    Adict = {}
    for i in A:
        if i in Adict:
            Adict[i] += 1
        else:
            Adict[i] = 1
            
    if len(Adict) <= K:
        print(0)
        sys.exit()
        
    #print(Adict)
    i = 0
    ans = 0
    for k, v in sorted(Adict.items(), key=lambda x: -x[1]):
        #print("{} {}".format(k,v))
        if i < K:
            i += 1
            continue
        #print(k)
        ans += v
        
    print(ans)
            	
if __name__ == "__main__":
	main()
