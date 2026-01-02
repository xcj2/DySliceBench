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
    N = I()
    A = [LI() for i in range(N)]

    dq = []
    heapify(dq)
    
    for i in range(N):
        for j in range(N):
            heappush(dq, (A[i][j], i, j))
    
    # dist matrix
    dist = [[float('inf') if i != j else 0 for i in range(N)] for j in range(N)]
    
    res = 0
    
    while dq:
        d, x, y = heappop(dq)
        equal = True
        for i in range(N):
            tempD = dist[x][i]+dist[i][y]
            if d > tempD:
                print(-1)
                exit()
            elif d == tempD:
                equal = False
    
        dist[x][y] = d
        dist[y][x] = d
    
        if equal:
            res+=d

    print(res)

if __name__ == "__main__":
    main()