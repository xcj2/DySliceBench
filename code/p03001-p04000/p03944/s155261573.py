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
    W,H,N = inputMap()
    x_hidari = 0
    x_migi = W
    y_shita = 0
    y_ue = H
    
    for i in range(N):
        x,y,a = inputMap()
        
        if a == 1:
            if x_hidari < x:
                x_hidari = x
        elif a == 2:
            if x_migi > x:
                x_migi = x
        elif a == 3:
            if y_shita < y:
                y_shita = y
        else:
            if y_ue > y:
                y_ue = y
                
    #print("{} {} {} {}".format(x_hidari,x_migi,y_ue,y_shita))
    xxx = x_migi-x_hidari
    yyy = y_ue-y_shita
    if xxx < 0 or yyy < 0:
        print(0)
        sys.exit()
    
    print(xxx * yyy)
    
    
if __name__ == "__main__":
	main()
