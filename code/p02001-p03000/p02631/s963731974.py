#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
def resolve():
    N,=pin()
    A=lispin()
    #累積を入れて引き算でいけ
    left=[0]*N
    left[-2]=A[-1]    

    temp=0
    for i in A:
        temp=temp^i
    left[-1]=temp
    #print(left)

    left[0]=A[0]^left[-1]
    #print(left)

#    left[1]=11^left[-1]^left[0]
#    print(left)
    for i in range(1,N-2):
        left[i]=A[i]^left[-1]^left[i-1]
    #output
    ans=[left[0]]
    for i in range(1,N):
        ans.append(left[i]^left[i-1])
    print(*ans)
#%%submit!
resolve()
