#from math import *
from collections import *
from random import *
from bisect import *
import sys
input=sys.stdin.readline
def lis():
    return list(map(int,input().split()))
def ma():
    return map(int,input().split())
def inp():
    return int(input())
n=inp()
s=input().rstrip('\n')
x=s.count('R')
if(x==0 or x==n):
    print(0)
    exit(0)
ind=[]
for i in range(n):
    if(s[i]=='R'):
        ind.append(i)
r=0
for i in range(x):
    if(s[i]=='R'):
        continue
    r+=1
print(r)
            

        
            
        
    
        
    
