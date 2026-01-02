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
    F = [[[0 for _ in range(2)] for _ in range(5)] for _ in range(N)]
    for i in range(N):
        tmp = inputList()
        for j,val in enumerate(tmp):
            ind = j // 2
            if j % 2 == 0:
                F[i][ind][0] = val
            else:
                F[i][ind][1] = val
                
    P = []
    for i in range(N):
        tmp = inputList()
        P.append(tmp)
        
    ans = -100000000000000000000000000
    for i in range(1, 2**10):
        ans_tmp = [0 for _ in range(N)]
        for j in [1,2,2**2,2**3,2**4,2**5,2**6,2**7,2**8,2**9]:
            tmp = j & i
            ind = 0
            hi = 0
            
            if tmp == 0:
                ind = -1
                hi = -1
            elif tmp == 1:
                ind = 0
                hi = 0
            elif tmp == 2:
                ind = 0
                hi = 1
            elif tmp == 4:
                ind = 1
                hi = 0
            elif tmp == 8:
                ind = 1
                hi = 1
            elif tmp == 16:
                ind = 2
                hi = 0
            elif tmp == 32:
                ind = 2
                hi = 1
            elif tmp == 64:
                ind = 3
                hi = 0
            elif tmp == 128:
                ind = 3
                hi = 1
            elif tmp == 256:
                ind = 4
                hi = 0
            elif tmp == 512:
                ind = 4
                hi = 1
                
            if ind != -1:
                for k in range(N):
                    tmp2 = F[k][ind][hi]
                    #if k == 0:
                        #print("{} {} {}".format(k,ind,hi))
                    #if i == 683:
                        #print("{} {} {}".format(k,ind,hi))
                    if tmp2 == 1:
                        ans_tmp[k] += 1
                        
        a_tmp = 0
        for j in range(N):
            a_tmp += P[j][ans_tmp[j]]
        if ans < a_tmp:
            ans = a_tmp
        
    print(ans)
            	
if __name__ == "__main__":
	main()
