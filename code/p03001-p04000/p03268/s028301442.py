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


def main():
    N, K = MI()
    num_factor_K = N // K
    ret = num_factor_K ** 3
    
    if K % 2 == 0:
        num_factor_half_K = N // K
        if N % K >= K // 2:
            num_factor_half_K += 1
        ret += num_factor_half_K ** 3
        
    print(ret)
    

if __name__ == "__main__":
    main()