# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    class BIT:
        def __init__(self,n):
            self.num=n
            self.dat=[0]*(self.num+1)
            self.depth=n.bit_length()
        
        def add(self,i,x):
            i+=1
            while i<=self.num:
                self.dat[i]+=x
                i+=i&-i
        
        def sum(self,i):
            i+=1
            s=0
            while i>0:
                s+=self.dat[i]
                i-=i&-i
            return s
        
        def lower_bound(self,x):
            sum_=0
            pos=0
            for i in range(self.depth,-1,-1):
                k=pos+(1<<i)
                if k<=self.num and sum_+self.dat[k]<x:
                    sum_+=self.dat[k]
                    pos+=1<<i
            return pos, sum_
    
    N,Q=map(int,input().split())
    S,T,X=[0]*N,[0]*N,[0]*N
    for i in range(N):
        S[i],T[i],X[i]=map(int,input().split())
    unique_X=sorted(list(set(X)))
    d={unique_X[i]:i for i,x in enumerate(unique_X)}
    l=[0]*(N*2+Q)
    for i in range(N):
        l[i*2]=((S[i]-X[i])<<40)+(1<<20)+d[X[i]]
        l[i*2+1]=((T[i]-X[i])<<40)+d[X[i]]
    for i in range(N*2,N*2+Q):
        l[i]=(int(input())<<40)+(2<<20)
    l.sort()
    mask=(1<<20)-1
    b=BIT(len(unique_X))
    for tqx in l:
        x=tqx&mask
        q=(tqx>>20)&mask
        t=(tqx>>40)&mask
        if q==0:
            b.add(x,-1)
        elif q==1:
            b.add(x,1)
        else:
            res,_=b.lower_bound(1)
            print(unique_X[res] if res<len(unique_X) else -1)
        


if __name__ == '__main__':
    main()
