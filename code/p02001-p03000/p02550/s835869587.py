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
    N, X, M = MI()
    S = list([X])
    num = X
    for i in range(N-1):
        num = (num**2) % M
        if not num in S:
            S.append(num)
        else:
            break

    len_s = len(S)
    if len_s == N:
        print(sum(S))
    else:
        index_s = S.index(num)
        #循環を開始する前までの個数
        num1 = index_s
        sum1 = sum(S[0:index_s])
        
        #循環後
        num2 = len_s - index_s
        sum2 = sum(S)-sum1
        
        #循環する個数
        num3 = (N-num1) // num2
        sum3 = sum2 * num3
        
        #あまり
        num4 = (N-num1) % num2
        sum4 = sum(S[index_s:index_s+num4])
        
        ans = sum1+sum3+sum4
        print(ans)
    
    
if __name__ == "__main__":
    main()