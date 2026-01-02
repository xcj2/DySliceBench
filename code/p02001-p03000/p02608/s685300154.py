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
def si():return input()
def mi():return map(int,input().split())
def li():return list(mi())
abc='abcdefghijklmnopqrstuvwxyz'
mod=1000000007
# mod=998244353
inf = float("inf")
vow=['a','e','i','o','u']
dx,dy=[-1,1,0,0],[0,0,1,-1]

def bo(i):
    return ord(i)-ord('a')

file=0




def f(x,y,z):
    return (x*x)+(y*y)+(z*z)+(x*y)+(y*z)+(z*x)
def solve():


    # for _ in range(ii()):
    
        

    n=ii()
    ans=[0]*(n+1)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if f(i,j,1)>n:
                break
            for k in range(1,n+1):
                x=f(i,j,k)
                if x>n:
                    break
                ans[x]+=1

    for i in range(1,n+1):
        print(ans[i])





        
if __name__ =="__main__":

    if(file):

        if path.exists('input1.txt'):
            sys.stdin=open('input1.txt', 'r')
            sys.stdout=open('output1.txt','w')
        else:
            input=sys.stdin.readline
    solve()
