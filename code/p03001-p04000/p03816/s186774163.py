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
    A.sort()
    dic = {}
    
    for i,val in enumerate(A):
        if val in dic:
            dic[val] += 1
        else:
            dic[val] = 1
            
    delet = []
    for k, v in dic.items():
        if v > 1:
            tmp = v - 1
            for _ in range(tmp):
                delet.append(k)
                
    tmp = -(-len(delet) // 2)
    ans = N
    ans = ans - (tmp * 2)
        
    print(ans)
    
            
            
if __name__ == "__main__":
	main()
