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
    S = input()
    
    left = 0
    right = 0
    for s in S:
        if s == '(':
            left += 1
        else:
            if left > 0:
                left -= 1
            else:
                right += 1
    ret = '(' * right + S + ')' * left
    print(ret)

if __name__ == "__main__":
    main()