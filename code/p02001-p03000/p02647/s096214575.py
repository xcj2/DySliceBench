#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
def resolve():
    # 愚直解
    N,K=pin()
    A=lispin()
    B=[0]*N
    B[0]=A[0]
    for j in range(1,N):
        B[j]=A[j]-A[j-1]
    #print(B)

    for k in range(K):
        temp=0
        C=[0]*N
        for i in range(N):
            temp+=B[i]
            #print(temp)
            if i-temp<0:

                C[0]+=1
            else:C[i-temp]+=1

            if i+temp+1<N:
                C[i+temp+1]-=1
        B=C[:]
        if B[0]==N and sum(B)==N:
            break
    ans=[]
    x=0
    for c in C:
        x+=c
        ans.append(x)
    print(*ans)
    #after contest
    
#%%submit!
resolve()