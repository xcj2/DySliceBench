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

file=0



def solve():
    
    # for _ in range(ii()):
    h,w,k=mi()
    a=[]
    cnt=0
    for i in range(h):
        a.append(si())
        for j in a[i]:
            if j=='#':
                cnt+=1
    ans=0
    # print(cnt)
    for i in range(1<<(h+w)):
        c=set()
        x=[]
        y=[]
        for j in range(h):
            if (i>>j)&1:
                x.append(j)
                for k1 in range(w):
                    if a[j][k1]=='#':
                        c.add(tuple([j,k1]))
        for j in range(w):
            if (i>>(h+j))&1:
                for k1 in range(h):
                    if a[k1][j]=='#':
                        c.add(tuple([k1,j]))
        c1=cnt-len(c)
        if(c1==k):
            # print(c,i,x,y)
            ans+=1
        
    print(ans)



 









if __name__ =="__main__":

    if(file):

        if path.exists('input1.txt'):
            sys.stdin=open('input1.txt', 'r')
            sys.stdout=open('output1.txt','w')
        else:
            input=sys.stdin.readline
    solve()
