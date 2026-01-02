from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
from itertools import permutations,groupby
import sys
import bisect
import string
alp=string.ascii_lowercase
sys.setrecursionlimit(10**6)
def SI():
    return input().split()
def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]
YN=['Yes','No']
mo=10**9+7
#mo=998244353
#input=sys.stdin.readline

n=I()
s=list(input())
ans=0
t=[]
l,r=0,0
for i in range(n*2):
    if i==0:
        t+=['L']
        l+=1
        continue
    if ((l-r)%2==1 and s[i]=='W') or ((l-r)%2==0 and s[i]=='B'):
        t+=['L']
        l+=1
    else:
        t+=['R']
        r+=1
if t.count('L')!=n:
    print(0)
    exit()
    
#print(s,t)
L,R=0,0
ans=1
for i in t:
    if i=='L':
        L+=1
    if i=='R':
        ans*=L-R
        ans%=mo
        R+=1
f=1
for i in range(2,n+1):
    f*=i
    f%=mo
print((ans*f)%mo)

