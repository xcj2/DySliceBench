#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    A=[[] for _ in range(3)]
    for i in range(3):
        A[i]=LI()
    N=I()
    for _ in range(N):
        b=I()
        for i in range(3):
            for j in range(3):
                if A[i][j]==b:
                    A[i][j]=0
                    
    f=0
                
    for i in range(3):
        a=0
        for j in range(3):
            a+=A[i][j]
        if a==0:
            f=1
            
    for j in range(3):
        a=0
        for i in range(3):
            a+=A[i][j]
        if a==0:
            f=1
    a=0        
    for i in range(3):
        a+=A[i][i]
    if a==0:
        f=1
            
    a=A[2][0]+A[1][1]+A[0][2]
    if a==0:
        f=1
        
    if f==1:
        print("Yes")
    else:
        print("No")
            
    
        
        
            
        
                
        
    

main()
