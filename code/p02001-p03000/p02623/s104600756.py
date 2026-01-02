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




    
    
def solve():
    
    # for _ in range(ii()):
    n,m,k=mi()
    a=li()
    b=li()
    a1=a[:]
    b1=b[:]
    for i in range(1,n):
        a[i]+=a[i-1]
    for i in range(1,m):
        b[i]+=b[i-1]
    # print(a,b)
    i=0
    j=0
    # print(a,b)
    x1,y1=0,0
    while(k>0):
        x=bisect_right(a,k+x1,i,n)-1
        y=bisect_right(b,k+y1,j,m)-1
        if((x-i)>=(y-j)):
            if(k<a1[i]):
                break
            k-=a1[i]
            x1+=a1[i]
            i+=1
        else:
            if(k<b1[j]):
                break
            k-=b1[j]
            y1+=b1[j]
            j+=1
    print(i+j)

    
    
    
    
    
    
    
    
    
    
        
        
        
        
if __name__ =="__main__":

    if path.exists('input.txt'):
        sys.stdin=open('input.txt', 'r')
        sys.stdout=open('output.txt','w')
    else:
    	input=sys.stdin.readline
    solve()
