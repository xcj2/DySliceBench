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
    B = inputList()
    
    ans = 0
    for i, val in enumerate(A):
        if i == N:
            break
        if B[i] <= val:
            ans += B[i]
        else:
            tmp = B[i] - val
            ans += val
            if i-1 <= N-1:
                if tmp <= A[i+1]:
                    ans += tmp
                    A[i+1] -= tmp
                else:
                    ans += A[i+1]
                    A[i+1] = 0
                    
    print(ans)
            	
if __name__ == "__main__":
	main()
