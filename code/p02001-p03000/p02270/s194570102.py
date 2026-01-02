import bisect
import math
import sys
from collections import Counter, defaultdict, deque
from copy import copy, deepcopy
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations
from queue import Queue

read = sys.stdin.read
readline = sys.stdin.readline 
readlines = sys.stdin.readlines 

def SI():
    return int(readline())
def MI():
    return map(int, readline().split())
def MLI():
    return map(int, open(0).read().split())

inf = float("inf")
       
    
def check(k, P, W):
    count = 1
    tmp_sum = 0
    for w in W:
        if tmp_sum + w <= P:
            tmp_sum += w
        else:
            tmp_sum = w
            count += 1
    
    if count <= k:
        return True
    else:
        return False

def main():
    n, k, *W = MLI()
    
    lb = max(W)
    ub = sum(W)
    
    while ub - lb > 1:
        P = (lb + ub) // 2
        if check(k, P, W):
            ub = P
        else:
            lb = P
    
    if check(k, lb, W):
        print(lb)
    else:
        print(ub)
    
                
if __name__ == "__main__":
    main() 
