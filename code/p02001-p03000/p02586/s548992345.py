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
    r,c,k=MI()
    #dp=[[[-inf]*4 for j in range(c)]  for i in range(r)]
    dp0=[[-inf]*c for i in range(r)]
    dp1=[[-inf]*c for i in range(r)]
    dp2=[[-inf]*c for i in range(r)]
    dp3=[[-inf]*c for i in range(r)]
    val=[[0]*c for i in range(r)]
    for i in range(k):
        x,y,v=MI()
        val[x-1][y-1]=v
    if val[0][0]>0:
        dp1[0][0]=val[0][0]
        dp0[0][0]=0
    else:
        dp0[0][0]=0
    #print(dp)
    for i in range(r):
        for j in range(c):
            if i<r-1:
                if val[i+1][j]>0:
                        dp1[i+1][j]=max(dp1[i+1][j],dp0[i][j]+val[i+1][j],dp1[i][j]+val[i+1][j],dp2[i][j]+val[i+1][j],dp3[i][j]+val[i+1][j])
                dp0[i+1][j]=max(dp0[i+1][j],dp0[i][j],dp1[i][j],dp2[i][j],dp3[i][j])                 
            if j<c-1:
                if val[i][j+1]>0:
                    dp1[i][j+1]=max(dp1[i][j+1],dp0[i][j]+val[i][j+1])
                    dp2[i][j+1]=max(dp2[i][j+1],dp1[i][j]+val[i][j+1])
                    dp3[i][j+1]=max(dp3[i][j+1],dp2[i][j]+val[i][j+1])
                    #for k in range(1,4):
                        #dp[i][j+1][k]=max(dp[i][j+1][k],dp[i][j][k-1]+val[i][j+1])
                dp0[i][j+1]=max(dp0[i][j+1],dp0[i][j])
                dp1[i][j+1]=max(dp1[i][j+1],dp1[i][j])
                dp2[i][j+1]=max(dp2[i][j+1],dp2[i][j])
                dp3[i][j+1]=max(dp3[i][j+1],dp3[i][j])
                #for k in range(4):
                    #dp[i][j+1][k]=max(dp[i][j+1][k],dp[i][j][k])
    #print(dp0)
    #print(dp1)
    #print(dp2)
    #print(dp3)
    print(max(dp0[-1][-1],dp1[-1][-1],dp2[-1][-1],dp3[-1][-1]))
if __name__=="__main__":
    main()
    
            

