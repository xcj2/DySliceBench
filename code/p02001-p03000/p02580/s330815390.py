import sys
import bisect as bi
import math
from collections import defaultdict as dd
import heapq
import itertools
input=sys.stdin.readline
##import numpy as np
#sys.setrecursionlimit(10**7)
mo=10**9+7
def cin():
    return map(int,sin().split())
def ain():            
    return list(map(int,sin().split()))
def sin():
    return input()
def inin():
    return int(input())
##def power(x, y):
##    if(y == 0):return 1
##    temp = power(x, int(y / 2))%mo
##    if (y % 2 == 0):return (temp * temp)%mo 
##    else:
##        if(y > 0):return (x * temp * temp)%mo 
##        else:return ((temp * temp)//x )%mo
##
for _ in range(1):
    r,c,m=cin()
    d=dd(set)
    ro=[0]*r
    co=[0]*c
    for i in range(m):
        x,y=cin()
        ro[x-1]+=1
        co[y-1]+=1
        d[x-1].add(y-1)

    ans=0
    mar=[];mac=[]
    mar1=max(ro);mac1=max(co);
    for i in range(r):
        if(ro[i]==mar1):
            mar+=[i]
    for i in range(c):
        if(co[i]==mac1):
            mac+=[i]
##    print(mar ,mac)
    t=-1
    ans=mar1+mac1
    for i in mar:
        for j in mac:
            if(j not in d[i]):
                t=0
                break
    print(ans+t)
    
    
    
    
    

                    
                
    

    

        


    
        

    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
        
        
    
    
    
    


    





##
        
    
    
    
    
    
    
        
        
    
    
    
    


    





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
