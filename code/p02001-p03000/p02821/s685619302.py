from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
import math
import time
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
def ItoS(nn):
    return chr(nn+97)
def GI(V,E,Directed=False,index=0):
    org_inp=[]
    g=[[] for i in range(n)]
    for i in range(E):
        inp=LI()
        org_inp.append(inp)
        if index==0:
            inp[0]-=1
            inp[1]-=1
        if len(inp)==2:
            a,b=inp
            g[a].append(b)
            if not Directed:
                g[b].append(a)
        elif len(inp)==3:
            a,b,c=inp
            aa=(inp[0],inp[2])
            bb=(inp[1],inp[2])
            g[a].append(bb)
            if not Directed:
                g[b].append(aa)
    return g,org_inp
def bit_combination(k,n=2):
    rt=[]
    for tb in range(n**k):
        s=[tb//(n**bt)%n for bt in range(k)]
        rt+=[s]
    return rt
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
inf=float('inf')
l_alp=string.ascii_lowercase
u_alp=string.ascii_uppercase
ts=time.time()
#sys.setrecursionlimit(10**5)
input=lambda: sys.stdin.readline().rstrip()

def ran_input():
    import random
    n=random.randint(4,16)
    rmin,rmax=1,10
    a=[random.randint(rmin,rmax) for _ in range(n)]
    return n,a

show_flg=False
#show_flg=True

ans=0

n,m=LI()
a=sorted(LI())
ra=a[::-1]
##show(a,ra)

def Bigger(x,M): # x以上が M 個以上あるか
    cnt=0
    for i in range(n):
        y=x-ra[i]
        c=bisect.bisect(a,y-1)
        cnt+=n-c
##        show(x,a[i],y,cnt)
        if cnt>=M:
            return True
    return False

# function to check if x satisfies the condition
def check(x):
    if x==condition:
        rt=True
    else:
        rt=False
    return rt

# initial value
ng=1+a[-1]+a[-1]
ok=-1

while abs(ok-ng)>1:
    mid=(ok+ng)//2
    if Bigger(mid,m):
        ok=mid
    else:
        ng=mid

mean=ok
##show('ok=',ok,m)
# [ ok | ng ] is the boundary of the condition

##show(Bigger(67,3))

choice=0
for i in range(n):
    num=n-bisect.bisect(a,mean-a[i]-1)
    choice+=num
    ans+=num*a[i]*2
##    show('i,a[i],num,choice',i,a[i],num,choice)
##show('ans=')
#print(ans)
print(ans-mean*(choice-m))
