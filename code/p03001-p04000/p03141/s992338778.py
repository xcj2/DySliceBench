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
    N, *AB = MLI()
    
    happiness = defaultdict(list) 
    for A, B in zip(*[iter(AB)]*2):
        happiness[A+B].append((A, B))
        
    turn = -1
    score_A = 0
    score_B = 0
    for key in sorted(happiness.keys())[::-1]:
        values = deque(sorted(happiness[key]))
        while len(values) > 0:
            if turn == -1:
                A, B = values.pop()
                score_A += A
            else:
                A, B = values.popleft()
                score_B += B
            turn *= -1
            
    print(score_A - score_B)
    

if __name__ == "__main__":
    main()