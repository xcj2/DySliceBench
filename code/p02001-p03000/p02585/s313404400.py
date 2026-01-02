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
def end_of_loop():raise StopIteration

def main():
    N, K = MI()
    P = LI()
    C = LI()
    #1週下再に加算されるスコア並びにあるますから出発した際に１マス進んだ際のスコアがわかればよい。
    #初期化
    ans = []
    result = -float('inf')
    #開始点
    for i in range(N):
        result2= 0
        # start
        temp = i
        d = [-float('inf')] * N
        for j in range(N):
            temp = P[temp]-1
            result2+=C[temp]
            d[j] = result2
            if temp == i:
                index = j+1
                score = result2
                if index < K:
                    amari = K % index
                    syou = K // index
                    if amari !=0:
                        result = max(result, syou*score, syou*score+max(d[0:amari]), (syou-1)*score+max(d[0:index-1]), max(d), (syou-1)*score+max(d[0:index-1]))
                    else:
                        result = max(result, syou*score, max(d), (syou-1)*score+max(d[0:index-1]))
                    break
                else:
                    result = max(result, max(d[0:K]))
                    break
    print(result)

if __name__ == "__main__":
    main()