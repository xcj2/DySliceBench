from math import *
from collections import *
from itertools import *
from bisect import *
from operator import *
import sys
sys.setrecursionlimit(1000000)
def io():
    return map(int,input().split())
def op():
    return list(map(int,input().split()))
def o():
    return int(input())
def kl(con,x=0):
    if x==0:print('Yes') if con else print('No')
    elif x==1:print('yes') if con else print('no')
    elif x==2:print('YES') if con else print('NO')

MOD =    1000000007
MAX=2147483647
MIN=-2147483648
p=input
l,l1,l2,l3=[],[],[],[]
# for _ in range(o()):
n,k=io()
l=op()
x=y=0
i=0
fr=[0]*(200002)
while 1:
    if fr[l[i]]==0:
        l1.append(l[i])
        fr[l[i]]=1
        i=l[i]-1
    else:
        y=l1.index(l[i])
        x=len(l1)-y
        break
if k<=len(l1):
    print(l1[k-1])
else:
    k-=y
    k%=x
    if k==0:
        k=x
    print(l1[y+k-1])