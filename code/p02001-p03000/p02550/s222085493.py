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
mod=1000000007
# mod=998244353
inf = float("inf")
vow=['a','e','i','o','u']
dx,dy=[-1,1,0,0],[0,0,1,-1]

def bo(i):
    return ord(i)-ord('a')

def ceil(a,b):
    return (a+b-1)//b
file=1

def f():
    sys.stdout.flush()





def solve():

    # for _ in range(ii()):
   
    n,x,m = mi()  
    m1 = {}
    m1[x]=0
    a = [x]
    ans = x
    f  = 0
    for i in range(1,n):
        x = (x*x)%m
        if x in m1:
            now = i
            f = 1
            break
        m1[x] = i
        if x==0:
            print(ans)
            exit(0)
        ans += x
        a.append(x)
    if(f == 0):
        print(ans)
        exit(0)

    ans = 0
    for i in range(m1[x]):
        ans += a[i]
    b = []
    cnt = n - m1[x] 
    ans1 = 0
    x1 = cnt//(now-m1[x])
    cnt %= (now-m1[x])
    for i in range(m1[x],len(a)): 
        ans1 += a[i]
    k = m1[x]
    ans += (ans1*x1)
    for i in range(cnt):
        ans += a[k+i]
    print(ans)









        
if __name__ =="__main__":

   
    if path.exists('input.txt'):
        sys.stdin=open('input.txt', 'r')
        sys.stdout=open('output.txt','w')
    else:
        input=sys.stdin.readline
    solve()
    