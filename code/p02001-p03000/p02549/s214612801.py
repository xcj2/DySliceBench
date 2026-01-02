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
    N, K = MI()
    L = [LI() for i in range(K)]
    D = [0] * N
    D[0] = 1
    D[1] = -1
    num = 0
    mod = 998244353
    for index in range(N):
        num += D[index] % mod
        for l, r in L:
            if index + r + 1 <= N-1:
                D[index+l] += num
                D[index+r+1] -= num
            elif index+l <= N-1:
                D[index+l] += num
                
    print(num % mod)
    
if __name__ == "__main__":
    main()