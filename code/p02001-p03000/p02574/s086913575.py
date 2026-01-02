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
    mylist = LI()
    max_num = max(mylist)
    max_num2 = math.ceil(math.sqrt(max_num))
    D = [True]* (max_num+1)
    D[0] = D[1] = False
    mylist = Counter(mylist)
    setwise = True
    pairwise = True

        
    for i in range(2, max_num+1):
        temp = 0
        if D[i]:
            for j in range(i, max_num+1, i):
                D[j] = False
                
                try:
                    temp+=mylist[j]
                except:
                    pass

            if temp == N:
                print("not coprime")
                sys.exit()
            if temp >= 2:
                pairwise = False

    if pairwise:
        print("pairwise coprime")
    else:
        print("setwise coprime")
                    

            
    
    
if __name__ == "__main__":
    main()