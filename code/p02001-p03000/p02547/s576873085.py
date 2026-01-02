
import sys
import bisect as bi
import math
from collections import defaultdict as dd
import heapq
import itertools
##import operator
input=sys.stdin.readline
import random
##sys.setrecursionlimit(10**6)
##fo=open("output1.txt","w")
##fi=open("input1.txt","w")
mod=10**9+7
def cin():
    return map(int,sin().split())
def ain():            
    return list(map(int,sin().split()))
def sin():
    return input()
def inin():
    return int(input())

    
for _ in range(1):
    n=inin();cont=0;f=0
    for i in range(n):
        a,b=cin()
        if(a==b):
            cont+=1
        else:
            cont=0
        if(cont==3):
            f=1
    if(f):print("Yes")
    else:print("No")
    

    
    
        
        
      
    

##def msb(n):n|=n>>1;n|=n>>2;n|=n>>4;n|=n>>8;n|=n>>16;n|=n>>32;n|=n>>64;return n-(n>>1) #2 ki power
##def pref(a,n,f):             
##    pre=[0]*n
##    if(f==0):         ##from beginning
##        pre[0]=a[0]
##        for i in range(1,n):
##            pre[i]=a[i]+pre[i-1]
##    else:              ##from end
##        pre[-1]=a[-1]
##        for i in range(n-2,-1,-1):
##            pre[i]=pre[i+1]+a[i]
##    return pre
##maxint=10**24 
##def kadane(a,size): 
##    max_so_far = -maxint - 1
##    max_ending_here = 0
##       
##    for i in range(0, size): 
##        max_ending_here = max_ending_here + a[i] 
##        if (max_so_far < max_ending_here): 
##            max_so_far = max_ending_here 
##  
##        if max_ending_here < 0: 
##            max_ending_here = 0   
##    return max_so_far
