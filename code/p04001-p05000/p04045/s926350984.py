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
    N,K = inputMap()
    D = inputList()
    
    base = list(range(10))
    for vol in D:
        base.remove(vol)
        
    ans = ""
    NN = str(N)
    flg = False
    for i,val in enumerate(NN):
        isInp = False
        for j,vol in enumerate(base):
            if flg == True:
                ans += str(vol)
                isInp = True
                break
            tmp = int(val)
            if tmp == vol:
                ans += val
                isInp = True
                break
            elif tmp < vol:
                flg = True
                ans += str(vol)
                isInp = True
                break
            else:
                continue
        
        if isInp == False:
            ans += "*"
    
    if "*" not in ans:
        print(ans)
        sys.exit()
    
    ans = list(ans)
    ans_T = ""
    if ans[0] == "*" or 1 == 1:
        if base[0] != 0:
            ans_T += str(base[0])
        else:
            ans_T += str(base[1])
        for i in range(len(str(N))):
            ans_T += str(base[0])
        print(ans_T)
        sys.exit()
    
if __name__ == "__main__":
	main()
