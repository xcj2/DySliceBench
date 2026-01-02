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


class Dictionary:
    def __init__(self):
        self.dict = defaultdict(lambda:False)
    
    def insert(self, x):
        self.dict[x] = True
        
    def find(self, x):
        if self.dict[x]:
            print("yes")
        else:
            print("no")
            
            
def main():
    Dict = Dictionary()
    
    n = int(input())
    for i in range(n):
        op, key = input().split()
        if op == "find":
            Dict.find(key)
        else:
            Dict.insert(key)

if __name__ == "__main__":
    main() 
