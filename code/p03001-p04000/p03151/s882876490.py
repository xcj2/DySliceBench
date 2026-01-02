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
    B = inputList()
    
    A_sum = 0
    for i in A:
        A_sum += i
    
    B_sum = 0
    for i in B:
        B_sum += i
        
    if A_sum < B_sum:
        print(-1)
        sys.exit()
        
    tarinai = []
    tariteru = []
    flg = False
    for i in range(N):
        if A[i] < B[i]:
            tarinai.append(B[i] - A[i])
            tariteru.append(0)
            flg = True
        else:
            tarinai.append(0)
            tariteru.append(A[i] - B[i])
            
    if flg == False:
        print(0)
        sys.exit()
        
    tariteru.sort()
    tariteru = tariteru[::-1]
            
    ans = 0
    tameru = 0
    for i in tarinai:
        if i == 0:
            continue
        ans += 1
        tameru += i
        
    for i in tariteru:
        ans += 1
        tameru -= i
        if tameru <= 0:
            break
            
    print(ans)
    
if __name__ == "__main__":
	main()
