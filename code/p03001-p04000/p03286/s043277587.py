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
    N = SI()
    
    if N == 0:
        print(0)
    else:
        ret = ''
        cursor = 1
        devide = 2
        while N != 0:
            if N % devide == 0:
                ret = '0' + ret
            else:
                ret = '1' + ret
                N -= cursor
            cursor *= -2
            devide *= 2
        
        print(ret)

if __name__ == "__main__":
    main()