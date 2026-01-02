'''
    Auther: ghoshashis545 Ashis Ghosh
    College: jalpaiguri Govt Enggineering College

'''
from os import path
import sys
from heapq import heappush,heappop
from functools import cmp_to_key as ctk
from collections import deque,defaultdict as dd 
from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
from itertools import permutations
from datetime import datetime
from math import ceil,sqrt,log,gcd
def ii():return int(input())
def si():return input().rstrip()
def mi():return map(int,input().split())
def li():return list(mi())
abc='abcdefghijklmnopqrstuvwxyz'
# mod=1000000007
mod=998244353
inf = float("inf")
vow=['a','e','i','o','u']
dx,dy=[-1,1,0,0],[0,0,1,-1]

def bo(i):
    return ord(i)-ord('a')



    
def solve():

    
    # for _ in range(ii()):

    n,k = mi()

    seg = []

    for i in range(k):
        seg.append(li())

    dp = [0]*(n+1)

    dp[1] = 1
    for i in range(2,n+1):
        dp[i] += dp[i-1]
        dp[i] %= mod
        for j in range(k):
            if seg[j][0] >= i:
                continue


            l = max(1,i - seg[j][1])

            r =  i - seg[j][0]

            dp[i] += dp[r] - dp[l-1]
            dp[i] += mod
            dp[i] %= mod


    print((dp[n] - dp[n-1] + mod)%mod)


        









        
if __name__ =="__main__":

    
    if path.exists('input.txt'):
        sys.stdin=open('input.txt', 'r')
        sys.stdout=open('output.txt','w')
    else:
        input=sys.stdin.readline
    solve()