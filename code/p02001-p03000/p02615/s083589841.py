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

file = 0

def solve():
    



    # for _ in range(ii()):

    n=ii()
    a=li()
    a.sort(reverse=True)
    if(n==1):
        print(0)
        exit(0)
    ans=a[0]
    k=n-2
    for i in range(1,n):
        if(k==0):
            break
        if(k==1):
            ans+=a[i]
            k-=1
        else:
            ans+=2*a[i]
            k-=2
    print(ans)










  
















if __name__ =="__main__":

    if(file):

        if path.exists('input1.txt'):
            sys.stdin=open('input1.txt', 'r')
            sys.stdout=open('output1.txt','w')
        else:
            input=sys.stdin.readline
    solve()