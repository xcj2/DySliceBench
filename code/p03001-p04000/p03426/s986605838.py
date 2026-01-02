#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    H,W,D=pin()
    precal_magicalresource=[]#D series
    places_num=[None]*(H*W+1)
    for h in range(1,H+1):
        temp=tupin()
        for w in range(1,W+1):
            places_num[temp[w-1]]=(h,w)
    places_num[0]=(0,0)
    #print(places_num)

    for d in range(D):#about Li%D
        d_mag=[]
        d_mag.append(0)
        temp=places_num[d]
        p=0
        while(1):
            d+=D
            if d>H*W:break
        
            s=abs(temp[0]-places_num[d][0])
            t=abs(temp[1]-places_num[d][1])
            p+=s+t
            d_mag.append((p))
            temp=places_num[d]
        precal_magicalresource.append(d_mag)
        #print(precal_magicalresource)
    Q=int(input())    
    for q in range(Q):
        l,r=pin()
        lm=l%D
        rd=r//D
        ld=l//D
        print(precal_magicalresource[lm][rd]-precal_magicalresource[lm][ld])
#%%submit!
resolve()