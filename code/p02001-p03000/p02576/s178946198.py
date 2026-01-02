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
    N, X, T = MI()
    if N % X == 0:
        print((N//X)*T)
    else:
        print(((N//X)+1)*T)
if __name__ == "__main__":
    main()