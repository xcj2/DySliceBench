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
def LI(): return tuple(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]
def end_of_loop():raise StopIteration
    
    
def main():
    N, M = MI()
    Switch = [LI() for i in range(M)]
    P = LI()
    result = 0
    for i in range(2**N):
        result += 1
        for index, swich in enumerate(Switch):
            if swich[0] == 0:
                continue
            temp = 0
            for j in range(swich[0]):
                if i >> (swich[j+1]-1) & 1 == 1:
                    temp += 1
            if temp % 2 != P[index]:
                result-=1
                break
            
    print(result)
                    
                    
            
            
        
if __name__ == "__main__":
    main()