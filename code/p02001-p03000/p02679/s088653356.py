def modpow(a,n,p):
    if n==0:
        return 1
    x=modpow(a,n//2,p)
    x=(x*x)%p
    if (n%2)==1:
        x=(x*a)%p
    return x%p
def modinv(a,p):
    return modpow(a,p-2,p)
def ggcd(a,b):
    if(b==0):
        return a
    return ggcd(b,a%b)
import math
import fractions
import collections
import itertools
import pprint
N=int(input())
l1=[]
adivb=[]
bis0=0
bdiva=[]
ais0=0
both0=0
p=10**9+7
fish=[list(map(int,input().split())) for _ in range(N)]
fishcomp=[]
d={}
for i in range(N):
    a=fish[i][0]
    b=fish[i][1]
    g=ggcd(a,b)
    if g!=0:
        a=a//g
        b=b//g
    if b<0:
        a=-a
        b=-b
    if (a!=0)or(b!=0):
        if d.get(a)==None:
            d[a]={}
            d[a][b]=1
        else:
            if d[a].get(b)==None:
                d[a][b]=1
            else:
                val=d[a].get(b)
                d[a][b]=val+1
        fishcomp.append([a, b])
    else:
        both0=both0+1
#print(d)
#print(fishcomp)
fishcomp=list(map(list,set(map(tuple,fishcomp))))
#print(fishcomp)
length=N-both0
sets=[]
for i in fishcomp:
    a=i[0]
    b=i[1]
    val1=d[a][b]
    #print(a,b,val1)
    if d.get(-b)!=None:
        if d[-b].get(a)!=None:
            val2=d[-b][a]
            sets.append([val1,val2])
            length=length-(val2+val1)
#print(sets,length)
pro=1
for i in sets:
    pro=(pro*(pow(2,i[0],p)+pow(2,i[1],p)-1))%p
#print(pro)
print((pow(2,length,p)*pro-1+both0)%p)
