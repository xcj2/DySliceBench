# -*- coding: utf-8 -*-
import sys
import copy
import collections
from bisect import bisect_left
from bisect import bisect_right
from collections import defaultdict
from heapq import heappop, heappush
import math
import itertools

# NO, PAY-PAY
#import numpy as np
#import statistics
#from statistics import mean, median,variance,stdev

def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))
 
def main():
    N,M,R = inputMap()
    r = inputList()
    A = [[100000000000000000 for _ in range(N)] for _ in range(N)]
    
    for _ in range(M):
        a,b,c = inputList()
        A[a-1][b-1] = c
        A[b-1][a-1] = c
    
    for i in range(N):
        A[i][i] = 0
        
    A = warshall_floyd(A, N)
        
    ans = -1
    visi = list(itertools.permutations(r))
    for sp in visi:
        tmp = 0
        for i, val in enumerate(sp):
            if i == 0:
                continue
            tmp += A[sp[i-1]-1][sp[i]-1]
            
        if ans == -1 or ans > tmp:
            ans = tmp
            
    print(ans)
        
def warshall_floyd(d, n):
	#d[i][j]: iからjへの最短距離
	for k in range(n):
		for i in range(n):
			for j in range(n):
				d[i][j] = min(d[i][j], d[i][k] + d[k][j])
	return d
		
            	
if __name__ == "__main__":
	main()
