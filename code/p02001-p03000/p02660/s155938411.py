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
    if N==1:
        print(0)
        return

        
    n=int(N**0.5)+1
    divs=dict()
    temp=N
    for i in range(2,n+4):
        while (1):
            if temp%i !=0:
                break
            divs.setdefault(i,0)
            divs[i]+=1
            temp/=i
    if temp>1:
        divs.setdefault(temp,1)
    #print(divs)
    check=1
    ans=0
    for p,q in divs.items():
        check*=p**q
        temp2=0
        for i in range(1,50):
            temp2+=i
            if temp2>q:
                break
            ans+=1
            
            
        #print(ans)
    print(ans)
    assert N== check
    
#%%submit!
resolve()
