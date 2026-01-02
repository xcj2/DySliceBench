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
def LI(): return tuple(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]
    
    
def main():
    N = I()
    mylist = LI()
    shift = 1000000007
    S = sum(mylist)
    res = 0
    
    for i in mylist:
        S-=i
        if S==0:
            break
        res += (S*i)%shift
    

    print(int(res % shift))
    
if __name__ == "__main__":
    main()