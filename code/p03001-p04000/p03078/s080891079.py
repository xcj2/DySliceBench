# coding: utf-8
# hello worldと表示する
#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

def main():
    x,y,z,k=MI()
    set_=set()
    A=sorted(LI(),reverse=True)
    B=sorted(LI(),reverse=True)
    C=sorted(LI(),reverse=True)
    Q=[[(A[0]+B[0]+C[0])*(-1),0,0,0]]
    heapify(Q)
    set_.add((0,0,0))
    i=0
    ans=[]
    xl,yl,zl=0,0,0
    al=[]
    al=[[0,0,0]]
    while i<k:
        #print(Q)
        a,u,v,w=heappop(Q)
        ans.append([-a,u,v,w])
        print(-a)
        i+=1
        if u+1<x and (u+1,v,w) not in set_:
            heappush(Q,[-A[u+1]-B[v]-C[w],u+1,v,w])
            set_.add((u+1,v,w))
        if v+1<y and (u,v+1,w) not in set_:
            heappush(Q,[-A[u]-B[v+1]-C[w],u,v+1,w])
            set_.add((u,v+1,w))
        if w+1<z and (u,v,w+1) not in set_:
            heappush(Q,[-A[u]-B[v]-C[w+1],u,v,w+1])
            set_.add((u,v,w+1))
if __name__=="__main__":
    main()
    

    
    

    

    
    



    

    
    
