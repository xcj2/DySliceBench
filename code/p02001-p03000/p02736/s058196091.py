#dpでできないかな？
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,cos,radians,sqrt
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

n=I()
s=list(map(int,SI()))
if n==1:
    print(s[0])
    sys.exit()

def divi2(x):
    if x%2==1:
        return 0
    else:
        count=0
        while x%2==0:
            x//=2
            count+=1
        return count
#print(divi2(24))
pw2=[0 for i in range(n-1)]
for i in range(n-1):
    if i%2==1:
        pw2[i]=divi2(i+1)
#print(pw2)
#print(s)
cmbnk2=[0 for i in range(n)]
for i in range(n-1):
    cmbnk2[i+1]=cmbnk2[i]+pw2[n-2-i]-pw2[i]
#print(cmbnk2)
ans=0
'''if (s.count(1)==1 and not 2 in s ) or (s.count(3)==1 and not 2 in s ):
    ans=2
    print(ans)
    sys.exit()'''
if not 2 in s:
    for i in range(n):
        s[i]=(s[i]-1)//2
    for i in range(n):
        if cmbnk2[i]==0:
            ans+=s[i]%2
    if ans%2==0:
        print(0)
    else:
        print(2)
    sys.exit()
    
        
else:
    for i in range(n):
        if cmbnk2[i]==0:
            ans+=s[i]%2
            #print(s[i]%2)
        #print(cmbnk2[i]%2+1)
        #print(s[i])
print(ans%2)