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
    n, m = MI()
    mlist = LI()
    d = [[float('inf') if i != 0 else 0 for i in range(n+1)] for j in range(m+1)]
    for i, value in enumerate(mlist):
        for j in range(n+1):
            if j < value:
                d[i+1][j] = d[i][j]
            else:
                d[i+1][j] = min(d[i][j], d[i+1][j-value]+1)
    print(d[m][n])

        
    
if __name__ == "__main__":
    main()
