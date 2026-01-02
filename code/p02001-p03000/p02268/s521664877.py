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
    n = int(input())
    S = [i for i in MI()]
    
    q = int(input())
    T = [i for i in MI()]
    
    ret = 0
    for t in T:
        index = bisect.bisect_left(S, t)
        if index < n and S[index] == t:
            ret += 1
            
    print(ret)

if __name__ == "__main__":
    main()
