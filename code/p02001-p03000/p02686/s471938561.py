# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left,bisect_right
from collections import defaultdict
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    class SegmentTree:
        def __init__(self,n,segfunc,ide_ele):
            self.segfunc=segfunc
            self.ide_ele=ide_ele
            self.num=2**(n-1).bit_length()
            self.dat=[ide_ele]*2*self.num
        
        def init(self,iter):
            for i in range(len(iter)):
                self.dat[i+self.num]=iter[i]
            for i in range(self.num-1,0,-1):
                self.dat[i]=self.segfunc(self.dat[i*2],self.dat[i*2+1])
        
        def update(self,k,x):
            k+=self.num
            self.dat[k]=x
            while k:
                k//=2
                self.dat[k]=self.segfunc(self.dat[k*2],self.dat[k*2+1])
        
        def query(self,p,q):
            if q<=p:
                return self.ide_ele
            p+=self.num
            q+=self.num-1
            res=self.ide_ele
            while q-p>1:
                if p&1==1:
                    res=self.segfunc(res,self.dat[p])
                if q&1==0:
                    res=self.segfunc(res,self.dat[q])
                    q-=1
                p=(p+1)//2
                q=q//2
            if p==q:
                res=self.segfunc(res,self.dat[p])
            else:
                res=self.segfunc(self.segfunc(res,self.dat[p]),self.dat[q])
            return res
    
    N=int(input())
    S=[input() for i in range(N)]
    P=0
    M=0
    c=0
    Seg=SegmentTree(10**6+1,lambda a,b:max(a,b),-INF)
    l_PM=defaultdict(list)
    stack=defaultdict(list)
    minus=set()
    for i,s in enumerate(S):
        p=0
        m=0
        for x in s:
            if x=='(':
                p+=1
            else:
                if p>0:
                    p-=1
                else:
                    m+=1
        if m==0 and p>0:
            P+=p
        elif p==0 and m>0:
            M+=m
        elif p>0 and m>0:
            c+=1
            minus.add(m)
            stack[m].append(p-m)
    
    minus=list(minus)
    minus.sort()
    for x in minus:
        stack[x].sort()
        if x<=P:
            while stack[x]:
                y=stack[x].pop()
                if y>=0:
                    c-=1
                    P+=y
                else:
                    Seg.update(x,y)
                    l_PM[y].append(x)
                    break
        else:
            y=stack[x].pop()
            Seg.update(x,y)
            l_PM[y].append(x)
    
    for _ in range(c):
        x=Seg.query(0,P+1)
        if x==-INF or P+x<0:
            print('No')
            exit()
        
        l_PM[x].sort()
        
        res=bisect_right(l_PM[x],P)-1
        index=l_PM[x][res]
        del l_PM[x][res]
        if stack[index]:
            y=stack[index].pop()
            Seg.update(index,y)
            l_PM[y].append(index)
        else:
            Seg.update(index,-INF)
        P+=x
    P-=M
    YesNo(P==0)

if __name__ == '__main__':
    main()
