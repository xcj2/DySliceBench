# coding: UTF-8
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    class BIT():
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
    
    N=int(input())
    S=list(input())
    Q=int(input())
    bit=[BIT(N) for _ in range(26)]
    
    S2=[0]*N
    
    for i in range(N):
        S2[i]=ord(S[i])-ord('a')
    
    for i,x in enumerate(S2):
        bit[x].add(i,1)
    
    for _ in range(Q):
        a,b,c=input().split()
        if a=='1':
            b=int(b)-1
            c=ord(c)-ord('a')
            bit[c].add(b,1)
            bit[S2[b]].add(b,-1)
            S2[b]=c
        else:
            b=int(b)-1
            c=int(c)-1
            ans=0
            for i in range(26):
                if bit[i].sum(c)-bit[i].sum(b-1):
                    ans+=1
            print(ans)

if __name__ == '__main__':
    main()
