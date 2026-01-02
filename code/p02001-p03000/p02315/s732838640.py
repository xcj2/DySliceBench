import sys
import math
from collections import defaultdict, deque
from copy import deepcopy
    
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
    N, W = MI()
    mylist = [LI() for i in range(N)]
    d = [[0 for i in range(W+1)] for j in range(1+N)]
    for i in range(N):
        v, w = mylist[i]
        for j in range(W+1):
            if w > j:
                d[i+1][j] = max(d[i][j], d[i+1][j])
            else:
                d[i+1][j] = max(d[i][j], d[i+1][j], d[i][j-w]+v)
    print(d[N][W])
    
    
if __name__ == "__main__":
    main()
