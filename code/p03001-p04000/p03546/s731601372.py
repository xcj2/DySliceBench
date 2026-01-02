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
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]


def main():
    H, W = MI()
    D = defaultdict(int)
    
    cost = [LI() for i in range(10)]
    
    for i in range(H):
        temp = LI()
        for j in temp:
            if j != -1:
                D[j]+=1

    for i in range(10):
        for j in range(10):
            for k in range(10):
                cost[j][k] = min(cost[j][k], cost[j][i]+cost[i][k])
                
    ans = 0
    
    for key, num in D.items():
        ans += cost[key][1]*num
        
    print(ans)

    
if __name__ == "__main__":
    main()