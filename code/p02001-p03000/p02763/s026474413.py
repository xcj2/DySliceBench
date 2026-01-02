from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
import itertools
from functools import *
from itertools import permutations,combinations,groupby
import sys
import bisect
import string
import math
import time
import random
def Golf():
    *a,=map(int,open(0))
def S_():
    return input()
def IS():
    return input().split()
def LS():
    return [i for i in input().split()]
def I():
    return int(input())
def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]
def LI_():
    return [int(i)-1 for i in input().split()]
def NI(n):
    return [int(input()) for i in range(n)]
def NI_(n):
    return [int(input())-1 for i in range(n)]
def StoI():
    return [ord(i)-97 for i in input()]
def ItoS(nn):
    return chr(nn+97)
def LtoS(ls):
    return ''.join([chr(i+97) for i in ls])
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
def GGI(h,w,search=None,replacement_of_found='.',mp_def={'#':1,'.':0}):
#h,w,g,sg=GGI(h,w,search=['S','G'],replacement_of_found='.',mp_def={'#':1,'.':0}) # sample usage
    mp=[1]*(w+2)
    found={}
    for i in range(h):
        s=input()
        for char in search:
            if char in s:
                found[char]=((i+1)*(w+2)+s.index(char)+1)
                mp_def[char]=mp_def[replacement_of_found]
        mp+=[1]+[mp_def[j] for j in s]+[1]
    mp+=[1]*(w+2)
    return h+2,w+2,mp,found
def bit_combination(k,n=2):
    rt=[]
    for tb in range(n**k):
        s=[tb//(n**bt)%n for bt in range(k)]
        rt+=[s]
    return rt
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['YES','NO']
Yn=['Yes','No']
 
mo=10**9+7
inf=float('inf')
l_alp=string.ascii_lowercase
u_alp=string.ascii_uppercase
#ts=time.time()
#sys.setrecursionlimit(10**7)
input=lambda: sys.stdin.readline().rstrip()
 
def ran_input():
    import random
    n=random.randint(4,16)
    rmin,rmax=1,10
    a=[random.randint(rmin,rmax) for _ in range(n)]
    return n,a

def ran_input():
    import random
    n=random.randint(4,16)
    rmin,rmax=1,10
    a=[random.randint(rmin,rmax) for _ in range(n)]
    return n,a

# Binary Indexed Tree
# Bit.add(i,x)    : add x at i-th value
# Bit.sum(i)      : get sum up to i-th value
# Bit.l_bound(w)  : get lower bound of index where w can be inserted

class Bit:
    def __init__(self,n):
        self.size=n
        self.m=len(bin(self.size))-2
        self.arr=[0]*(2**self.m+1)
        
    def __str__(self):
        a=[self.sum(i+1)-self.sum(i) for i in range(self.size)]
        return str(a)
        
    def add(self,i,x):
        k=0
        while i<=self.size:
            k+=1
            self.arr[i]+=x
            i+=i&(-i)
        return
    
    def sum(self,i):
        rt=0
        while i>0:
            rt+=self.arr[i]
            i-=i&(-i)
        return rt
    
    def l_bound(self,w):
        if w<=0:
            return 0
        x=0
        k=2**self.m
        while k>0:
            if x+k<self.size and self.arr[x+k]<w:
                w-=self.arr[x+k]
                x+=k
            k//=2
        return x+1
        
    def u_bound(self,w):
        if w<=0:
            return 0
        x=0
        k=2**self.m
        while k>0:
            if x+k<self.size and self.arr[x+k]<=w:
                w-=self.arr[x+k]
                x+=k
            k//=2
        return x+1
        
class Bit0(Bit):
    def add(self,j,x):
        super().add(j+1,x)
    def l_bound(self,w):
        return max(super().l_bound(w)-1,0)
    def u_bound(self,w):
        return max(super().u_bound(w)-1,0)

class Multiset(Bit0):
    def __init__(self,max_v):
        super().__init__(max_v)
    def insert(self,x):
        super().add(x,1)
    def find(self,x):
        return super().l_bound(super().sum(x))
    def __str__(self):
        return str(self.arr)


show_flg=False
show_flg=True


n=I()
s=StoI()
q=I()

bt=[Bit0(n) for i in range(26)]


for i in range(n):
    bt[s[i]].add(i,1)

for _ in range(q):
    t,a,b=input().split()
    if t=='1':
        i,c=int(a)-1,ord(b)-97
        old=s[i]
        s[i]=c
        bt[c].add(i,1)
        bt[old].add(i,-1)
    else:
        l,r=int(a)-1,int(b)-1
        ans=0
        for i in range(26):
            if bt[i].sum(r+1)-bt[i].sum(l)>0:
                ans+=1
        print(ans)    

