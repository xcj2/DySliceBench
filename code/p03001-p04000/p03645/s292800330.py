#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    S=[0]*N
    for _ in range(M):
        a,b=MI()
        a-=1
        b-=1
        if a==0 or b==0:
            S[a+b]+=1
        if a==N-1 or b==N-1:
            S[a+b-(N-1)]+=1
            
    f=0
    for i in range(N):
        if S[i]==2:
            f=1
            
    if f==1:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
        

main()
