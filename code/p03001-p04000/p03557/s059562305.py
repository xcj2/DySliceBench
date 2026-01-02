#!/usr/bin/env pypy3
import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
import bisect


def main():
    mod=10**9+7
    
    N=I()
    A=[[] for _ in range(3)]
    for i in range(3):
        A[i]=LI()
        A[i].sort()
        
    BC=[0]*N
    
    for j in range(N):
        BC[j]=N-bisect.bisect_right(A[2], A[1][j])
                                    
    S=[0]*(N+1)
    for i in range(N):
        S[i+1]=S[i]+BC[i]
        
    ans=0
    for i in range(N):
        ans+=S[-1] - S[bisect.bisect_right(A[1],A[0][i])]
        
    print(ans)
    

main()
