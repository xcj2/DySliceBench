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
    s = inputInt()
    A = inputList()
    
    ans = -1
    for i in A:
        tmp_cont = 0
        tmp = i
        while True:
            if tmp % 2 != 0:
                break
            tmp = tmp // 2
            tmp_cont += 1
        #print("{}--{}".format(i, tmp_cont))
        if ans == -1 or ans > tmp_cont:
            ans = tmp_cont
        
    print(ans)
            	
if __name__ == "__main__":
	main()
