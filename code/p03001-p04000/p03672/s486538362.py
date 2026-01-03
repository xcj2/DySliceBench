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
 
# NO, PAY-PAY
#import numpy as np
#import statistics
#from statistics import mean, median,variance,stdev
 
def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))
 
def main():
    s = input()
    
    leng = len(s)
    
    for i in range(leng-1, -1, -1):
        testtest = s[0:i]
        
        tmp = is_run(testtest)
        if tmp == True:
            print(len(testtest))
            sys.exit()
            
    print(0)
    
    
    
def is_run(s):
    leng = len(s)
    if leng % 2 == 1:
        return False
        
    bese = int(leng/2)
    tmp1 = s[:bese]
    tmp2 = s[bese:]
    
    #print("{} {}".format(tmp1,tmp2))
    
    if tmp1 == tmp2:
        return True
    else:
        return False
        
if __name__ == "__main__":
	main()
