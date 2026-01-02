# coding: UTF-8
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    class SegmentTree:
        def __init__(self,n,ide_ele,segfunc):
            self.ide_ele=ide_ele
            self.segfunc=segfunc
            self.num=2**(n-1).bit_length()
            self.dat=[ide_ele]*2*self.num
        
        def init(self,iter):
            for i in range(n):
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
    S=list(input())
    Q=int(input())
    seg=[SegmentTree(N,0,lambda x,y:x+y) for _ in range(26)]
    
    S2=[0]*N
    
    for i in range(N):
        S2[i]=ord(S[i])-ord('a')
    
    for i,x in enumerate(S2):
        p=seg[x].query(i,i+1)
        seg[x].update(i,p+1)
    
    for _ in range(Q):
        a,b,c=input().split()
        if a=='1':
            b=int(b)-1
            c=ord(c)-ord('a')
            p=seg[c].query(b,b+1)
            seg[c].update(b,p+1)
            q=seg[S2[b]].query(b,b+1)
            seg[S2[b]].update(b,q-1)
            S2[b]=c
        else:
            b=int(b)-1
            c=int(c)-1
            ans=0
            for i in range(26):
                ans+=bool(seg[i].query(b,c+1))
            print(ans)

if __name__ == '__main__':
    main()
