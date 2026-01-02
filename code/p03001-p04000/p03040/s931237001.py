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
    
    Q=int(input())
    Query=[]
    unique_a=set()
    for _ in range(Q):
        q=tuple(map(int,input().split()))
        if q[0]==1:
            unique_a.add(q[1])
            Query.append(q)
        else:
            Query.append((q[0],0,0))
    unique_a=list(unique_a)
    unique_a.sort()
    d={x:i for i,x in enumerate(unique_a)}
    b0=BIT(len(unique_a))
    b1=BIT(len(unique_a))
    sum_b=0
    sum_a=0
    c=0
    for i,(q,a,b) in enumerate(Query,1):
        if q==1:
            b0.add(d[a],1)
            b1.add(d[a],a)
            c+=1
            sum_a+=a
            sum_b+=b
        else:
            index,_=b0.lower_bound(-(-c//2))
            x=unique_a[index]
            tmp=b1.sum(index)
            z=b0.sum(index)
            y=(z*2-c)*x-tmp*2+sum_a+sum_b
            print(x,y)

if __name__ == '__main__':
    main()
