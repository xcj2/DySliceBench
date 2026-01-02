# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    class SegmentTree():
        def __init__(self,n,ide_ele,segfunc):
            self.ide_ele=ide_ele
            self.segfunc=segfunc
            self.num=2**(n-1).bit_length()
            self.dat=[ide_ele]*2*self.num
        
        def init(self,iter):
            for i in range(n):
                self.dat[i+self.num-1]=iter[i]
            for i in range(self.num-2,-1,-1):
                self.dat[i]=self.segfunc(self.dat[2*i+1],self.dat[2*i+2])
        
        def update(self,k,x):
            k+=self.num-1
            self.dat[k]=x
            while k:
                k=(k-1)//2
                self.dat[k]=self.segfunc(self.dat[k*2+1],self.dat[k*2+2])
        
        def query(self,p,q):
            if q<=p:
                return self.ide_ele
            p+=self.num-1
            q+=self.num-2
            res=self.ide_ele
            while q-p>1:
                if p&1==0:
                    res=self.segfunc(res,self.dat[p])
                if q&1==1:
                    res=self.segfunc(res,self.dat[q])
                    q-=1
                p=p//2
                q=(q-1)//2
            if p==q:
                res=self.segfunc(res,self.dat[p])
            else:
                res=self.segfunc(self.segfunc(res,self.dat[p]),self.dat[q])
            return res
    
    n,q=map(int,input().split())
    seg=SegmentTree(n,INF,min)
    seg.init([2**31-1]*n)
    
    for _ in range(q):
        c,x,y=map(int,input().split())
        if c==0:
            seg.update(x,y)
        else:
            y+=1
            print(seg.query(x,y))

if __name__ == '__main__':
    main()

