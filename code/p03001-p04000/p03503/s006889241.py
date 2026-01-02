#!/usr/bin/env PyPy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
mod=10**9+7
import itertools

def main():
    N=I()
    F=[[] for _ in range(N)]
    P=[[] for _ in range(N)]
    
    for i in range(N):
        F[i]=LI()
        
    for i in range(N):
        P[i]=LI()
    
    def calc(L):
        temp=0
        for i in range(N):
            cnt=0
            for j in range(10):
                cnt+=L[j]*F[i][j]
            temp+=P[i][cnt]
            
        return temp
    
    ans=-1*(10**10)
    for ite in itertools.product([0,1], repeat=10):
        if sum(ite)!=0:
            ans=max(ans,calc(ite))

    print(ans)

main()
