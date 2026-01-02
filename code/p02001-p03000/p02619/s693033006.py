#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
def solve(LIST):
    ans=0
    last=[0]*26
    for i in range(len(LIST)):
        a=i+1 #day a0
        x=LIST[i]-1
        #increase        
        ans+=S[i][x]
        #decrease
        last[x]=a#update
        temp=0
        for j in range(26):
            temp+=C[j]*(a-last[j])
        #print(ans,temp,"deb")
        ans-=temp
        print(ans)
    
    return  
def resolve():
    global D,C,S
    #input of prob.A
    D,=pin()
    C=[*pin()]#0-indexed
    S=[[*pin()]for i in range(D)]

    #output of prob.A
    T=[int(input()) for i in range(D)]#0indexed
    solve(T)

    
#%%submit!
resolve()