# input = sys.stdin.readline
from bisect import *
from collections import *
from heapq import *
# import functools
# import itertools
# import math


mod=10**9+7
mod
ferumaC=10000
fac=[0 for i in range(ferumaC)]
fac[0]=1
ifac=[0 for i in range(ferumaC)]
ifac[0]=1
def mpow(x,n):
    num=1
    while n > 0:
        if n&1:
            num=num*x%mod
        x=x*x%mod
        n=n>>1
    return(num)

for i in range(0,ferumaC-1):
    fac[i+1]=(fac[i]*(i+1))%mod
    ifac[i+1]=ifac[i]*mpow(i+1,mod-2)%mod
def comb(a,b):
    if a==0 and b==0:return(1)
    if a<b or a<0:return(0)
    tmp=ifac[a-b]*ifac[b]%mod
    return(tmp*fac[a]%mod)



sosuulst={}
def soinsuu(i):
    for s in sosuulst:
        while i%s==0:
            sosuulst[s]+=1
            i//=s
    if i>1 and  not i in sosuulst :
        sosuulst.update({i:1})


N=int(input())
for i in range(2,N+1):
    soinsuu(i)


data=[sosuulst[i] for i in sosuulst]
#print(data)
count=0
for lst in [[2,4,4],[2,24],[4,14],[74]]:
    lst.reverse()
    flag=0
    temp=1
    if len(lst)<=2:
        for m,l in enumerate(lst):
            A=len([i for i in data if i>=l])-m
            if A<=0:
                flag=1
                break
            temp*=A


    else:
        A=len([i for i in data if i>=4])
        if A<=1:
            continue
        A=comb(A,2)
        temp*=A
        A=len([i for i in data if i>=2])-2
        if A<=0:
            continue
        temp*=A
    if not flag:
        #print(temp)
        count+=temp
print(count)
