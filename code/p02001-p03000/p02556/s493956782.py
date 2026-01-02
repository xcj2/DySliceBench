import sys
import math
from collections import defaultdict, deque, Counter
from copy import deepcopy
from bisect import bisect, bisect_right, bisect_left
from heapq import heapify, heappop, heappush
    
input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def TI(): return tuple(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]
    
    
def main():
    N = I()
    
    minA = minB = float('inf')
    maxA = maxB = - float('inf')
    
    for i in range(N):
        x, y = MI()
        x2, y2 = x - y, x + y
        minA = min(minA, x2)
        maxA = max(maxA, x2)
        minB = min(minB, y2)
        maxB = max(maxB, y2)
    
    print(max(maxA - minA, maxB - minB))
        
        
if __name__ == "__main__":
    main()