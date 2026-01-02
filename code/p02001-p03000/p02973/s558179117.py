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
    D = [float('inf')]*N
    for i in range(N):
        num = -I()
        index = bisect_right(D, num)
        D[index] = num

    res = 0
    for i in D:
        if i != float('inf'):
            res+=1
        else:
            break
    print(res)




if __name__ == "__main__":
    main()