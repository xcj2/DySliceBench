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
 
INF = float('inf')
def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))
 
def main():
    n = inputInt()
    a = inputList()
    aa = []
    for i,val in enumerate(a):
        if i == 0:
            aa.append(val)
        else:
            tmp = val + aa[i-1]
            aa.append(tmp)
            
    barans = 0
    ans = 0
    flg = True
    for i,val in enumerate(aa):
        if i == 0:
            if val <= 0:
                barans = 1 - val
                ans += barans
        else:
            val_sin = val + barans
            if flg == True:
                flg = False
                if val_sin >= 0:
                    tmp = 1 + val_sin
                    ans += tmp
                    barans -= tmp
            else:
                flg = True
                if val_sin <= 0:
                    tmp = 1 - val_sin
                    ans += tmp
                    barans += tmp
        
    barans = 0
    ansans = 0
    flg = False
    for i,val in enumerate(aa):
        if i == 0:
            if val >= 0:
                barans = 1 + val
                ansans += barans
                barans = -1 * barans
        else:
            val_sin = val + barans
            if flg == True:
                flg = False
                if val_sin >= 0:
                    tmp = 1 + val_sin
                    ansans += tmp
                    barans -= tmp
            else:
                flg = True
                if val_sin <= 0:
                    tmp = 1 - val_sin
                    ansans += tmp
                    barans += tmp
        
    #print("{} {}".format(ans, ansans))
    print(min(ans,ansans))
        
    
if __name__ == "__main__":
	main()
