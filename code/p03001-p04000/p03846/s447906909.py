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
    N = inputInt()
    A = inputList()
    base = []
    base_flg = []
    tmp = N // 2
    
    if N % 2 == 1:
        for i in range(0,N,2):
            base.append(i)
            base_flg.append(False)
    else:
        for i in range(1,N,2):
            base.append(i)
            base_flg.append(False)
            
    dic = {}
    for i in A:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    for k, v in dic.items():
        if k in base:
            if v == 2 and k != 0:
                ind = base.index(k)
                if base_flg[ind] == False:
                    base_flg[ind] = True
                else:
                    print(0)
                    sys.exit()
            else:
                if k == 0 and v == 1:
                    ind = base.index(k)
                    if base_flg[ind] == False:
                        base_flg[ind] = True
                    else:
                        print(0)
                        sys.exit()
                else:
                    print(0)
                    sys.exit()
        else:
            print(0)
            sys.exit()
            
    for i in base_flg:
        if i == False:
            print(0)
            sys.exit()
            
    tmp = N // 2    
    print((2**tmp) % 1000000007)
    
if __name__ == "__main__":
	main()
