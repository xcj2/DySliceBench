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
    N,M = inputMap()
    A = []
    for i in range(N):
        tmp = input()
        A.append(tmp)
        
    B = []
    for i in range(M):
        tmp = input()
        B.append(tmp)
        
    if N < M:
        print("No")
        sys.exit()
        
    if N == M:
        tmp1 = "".join(A)
        tmp2 = "".join(B)
        
        if tmp1 == tmp2:
            print("Yes")
        else:
            print("No")
        sys,exit()
        
    points = []
    AA = copy.deepcopy(A)
    for i,val in enumerate(AA):
        while True:
            tmp = run(val, B[0])
            if tmp != -1 and N-i >= M:
                points.append((i,tmp))
                valval = list(copy.deepcopy(val))
                valval[tmp] = "T"
                val = "".join(valval)
            else:
                break
            
    for i in points:
        lines, point = i
        flg = True
        for j,val in enumerate(B):
            tmp = A[lines+j][point:].find(val)
            if tmp == -1 or tmp != 0:
                flg = False
        
        if flg == True:
            print("Yes")
            sys.exit()
            
    print("No")
    
def run(ss, dd):
    return ss.find(dd)
    
if __name__ == "__main__":
	main()
