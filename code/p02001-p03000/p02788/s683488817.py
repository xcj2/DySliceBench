# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left,bisect_right
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    class RangeBIT:
        def __init__(self,n):
            self.p=self.BIT(n+1)
            self.q=self.BIT(n+1)
        
        def add(self,s,t,x):
            self.p.add(s,-x*s)
            self.p.add(t,x*t)
            self.q.add(s,x)
            self.q.add(t,-x)
        
        def sum(self,s,t):
            return self.p.sum(t)+self.q.sum(t)*t-self.p.sum(s)-self.q.sum(s)*s
        
        class BIT:
            def __init__(self,n):
                self.num=n
                self.dat=[0]*(self.num+1)
            
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

    N,D,A=map(int,input().split())
    X=[0]*N
    XH=[]
    for i in range(N):
        X[i],H=map(int,input().split())
        XH.append((X[i]-1,H))
    XH.sort()
    X.sort()
    l=[0]*N
    for i in range(N):
        l[i]=bisect_right(X,X[i]+D*2)-i
    
    b=RangeBIT(N)
    index=0
    ans=0
    while index<N:
        h=XH[index][1]-b.sum(index,index+1)
        if h<=0:
            index+=1
            continue
        d=-(-h//A)
        ans+=d
        b.add(index,index+l[index],d*A)
    print(ans)

if __name__ == '__main__':
    main()
