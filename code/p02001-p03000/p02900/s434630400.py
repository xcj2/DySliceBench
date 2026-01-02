from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
#import math
#import time
import random
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
sys.setrecursionlimit(10**6)
#input=sys.stdin.readline
show_flg=False
show_flg=True


def gcd(a,b):
    a,b=max(a,b),min(a,b)
    if a%b==0:
        return b
    rt=gcd(a%b,b)
    return rt

a,b=MI()
g=gcd(a,b)
og=g
ans=set()
ans.add(1)



for i in range(2,int(g**0.5)+2):
    if g%i==0:
        ans.add(i)
        while g%i==0:
            g//=i

x=len(ans)
if g>int(og**0.5) and og!=1:
    x+=1
    
print(x)
