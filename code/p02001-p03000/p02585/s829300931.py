'''
    Auther: ghoshashis545 Ashis Ghosh
    College: jalpaiguri Govt Enggineering College

'''
from os import path
import sys
from functools import cmp_to_key as ctk
from collections import deque,defaultdict as dd 
from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
from itertools import permutations
from datetime import datetime
from math import ceil,sqrt,log,gcd
def ii():return int(input())
def si():return input()
def mi():return map(int,input().split())
def li():return list(mi())
abc='abcdefghijklmnopqrstuvwxyz'
mod=1000000007
#mod=998244353
inf = float("inf")
vow=['a','e','i','o','u']
dx,dy=[-1,1,0,0],[0,0,1,-1]

def bo(i):
    return ord(i)-ord('a')


def fun(x,k):
    ans = -inf
    x += x
    n = len(x)
    for i in range(1,k+1):
        s = 0
        for j in range(i):
            s += x[j]
        l = 0
        ans = max(ans,s)
        for j in range(i,n):
            s += x[j]
            s -= x[l]
            l += 1
            ans = max(ans,s)
    return ans 



def solve():
    
    # for _ in range(ii()):

        


    n,k = mi()
    p = li()
    c = li()

    vis = [0]*(n+1)
    a = []
    for i in range(n):
        if vis[i]:
            continue
        x = []
        j = i
        while(vis[j]==0):
            vis[j] = 1
            x.append(c[p[j]-1])
            j = p[j]-1
        a.append(x)
    

    ans = -inf

    for i in a:
        s = sum(i)
        n = len(i)
        k1 = k
        if(k >= n):
            k1 = n 
        s1 = fun(i,k1)
        ans = max(ans,s1)
        if(k > n and s>0):
            s2 = (k//n)*s
            s2 += fun(i,k%n)
            ans = max(ans,s2)
            ans = max(ans,s1+(k//n-1)*s)
        ans = max(ans,s1)

    print(ans)
















        
if __name__ =="__main__":

    if path.exists('input.txt'):
        sys.stdin=open('input.txt', 'r')
        sys.stdout=open('output.txt','w')
    else:
        input=sys.stdin.readline
    solve()
