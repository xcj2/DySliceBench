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
    N = I()
    result = 0
    mylist = sorted(LI())
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if mylist[i] < mylist[j] and mylist[j] < mylist[k] and mylist[k] < mylist[i]+mylist[j]:                    
                    result+=1
    print(result)
    
if __name__ == "__main__":
    main()