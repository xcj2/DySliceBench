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
    
def fib(num):
    d = defaultdict(int)
    d[0] = 1
    d[1] = 1
    if num <= 1:
        return d[num]
    else:
        for i in range(1,num):
            d[i+1] = d[i]+d[i-1]
        return d[num]
    
    
    
def main():
    num = I()
    print(fib(num))
    
if __name__ == "__main__":
    main()
