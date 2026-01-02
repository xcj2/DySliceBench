from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
#import math
#import time
#import random
def I():
    return int(input())
def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]
def LI_():
    return [int(i)-1 for i in input().split()]
def StoI():
    return [ord(i)-97 for i in input()]
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
#ts=time.time()
#sys.setrecursionlimit(10**6)
#input=sys.stdin.readline
show_flg=False
show_flg=True

def naive(b,k):
    a=b*k
    n=len(a)
    
    p=a[0]
    t=0
    for i in range(n-1):
        if p==a[i+1]:
            t+=1
            p=-1
        else:
            p=a[i+1]
            
    return t


b=StoI()
a=b
k=I()
n=len(a)
p=a[0]
t=0

if len(b)*k<10:
    print(naive(b,k))
    exit()


for i in range(n-1):
    if p==a[i+1]:
        t+=1
        p=-1
    else:
        p=a[i+1]

odd=naive(b,3)-naive(b,1)
even=naive(b,4)-naive(b,2)
if k%2==1:
    ans=naive(b,1)+(k//2)*odd
else:


    ans=naive(b,2)+(k//2)*even-even
print(ans)
