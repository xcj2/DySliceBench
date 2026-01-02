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

s=input().rstrip().split("T")
x,y=MI()
    #print(s)
x0=len(s[0])
x=x-x0
X=[]
Y=[]
for i in range(1,len(s)):
    if i%2==1:
        Y.append(len(s[i]))
    else:
        X.append(len(s[i]))
#print(x,y)
#print(X)
#print(Y)
dpx=[[0]*(2*sum(X)+1) for i in range(len(X)+1)]
dpx[0][sum(X)]=1
for i in range(len(X)):
    for j in range(len(dpx[i])):
        if dpx[i][j]==1:
            dpx[i+1][j+X[i]]=1
            dpx[i+1][j-X[i]]=1
#print(dpx)
dpy=[[0]*(2*sum(Y)+1) for i in range(len(Y)+1)]
dpy[0][sum(Y)]=1
for i in range(len(Y)):
    for j in range(len(dpy[i])):
        if dpy[i][j]==1:
            dpy[i+1][j+Y[i]]=1
            dpy[i+1][j-Y[i]]=1
##print(sum(X)+x)
#print(sum(Y)+y)
if sum(X)+x<0 or sum(X)+x>=len(dpx[-1]) or sum(Y)+y<0 or sum(Y)+y>=len(dpy[-1]):
    print("No")
    sys.exit()
if dpx[-1][sum(X)+x]==1 and dpy[-1][sum(Y)+y]==1:
    print("Yes")
else:
    print("No")
    
    
    

    
    


    
    

        
        
    


    