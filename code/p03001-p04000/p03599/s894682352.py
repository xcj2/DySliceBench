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
    A,B,C,D,E,F = inputMap()
    A = A*100
    B = B*100
    
    ans_muzu = 0
    ans_satou = 0
    ans = -1
    
    for i in range(0, F, A):
        for j in range(0, F, B):
            for ii in range(0, F, C):
                for jj in range(0, F, D):
                    
                    if F < i + j + ii + jj:
                        continue
                        
                    mizu = i+j
                    satou = ii+jj
                    
                    if mizu == 0:
                        continue
                    
                    if satou / mizu > E / 100:
                        continue
                    
                    tmp = (satou / (satou+mizu)) * 100
                    if ans < tmp:
                        ans = tmp
                        ans_muzu = mizu
                        ans_satou = satou
                        
    print("{} {}".format(ans_muzu+ans_satou, ans_satou))
    
    
    
            	
if __name__ == "__main__":
	main()
