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
    N = inputInt()
    A = inputList()
    
    ans = [0]*N
    B=[]
    ans_str = ""
    for i in range(N, 0, -1):
        cons = 0
        for j in range(i, N+1, i):
            if ans[j-1] == 1:
                cons += 1
        if A[i-1] == 1 and cons % 2 == 0:
            ans[i-1] = 1
            B.append(i)
            #ans_str = ans_str + str(i) + " "
            continue
        if A[i-1] == 0 and cons % 2 == 1:
            ans[i-1] = 1
            B.append(i)
            #ans_str = ans_str + str(i) + " "
            continue
            
    print(len(B))
    print(*B)
            	
if __name__ == "__main__":
	main()
