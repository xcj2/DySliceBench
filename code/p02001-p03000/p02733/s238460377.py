#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    H,W,K=pin()
    choco=[list(input()) for _ in range(H)]
    #think H<=10:bit full search
    ans=H+W #default
    #print(choco)
    for h in range(1<<(H-1)):#uekara h banme no yoko de waru
        tempans=0

        see=[]

        shiro=[0]
        for i in range(H):
            see.append(tempans)
            if (1<<i)&h:
                tempans+=1 
                shiro.append(0)
            
        #print(see,tempans,bin(h),"sth")
        #print(shiro,";")
        #yokoni krenai nara donkoku de jituhatokeru
        j=0
        while(j<W):
            f=1
            for n,s in enumerate(see):
                shiro[s]+=int(choco[n][j])
                if shiro[s]>K:#suguhidaride kiru
                    if j==0:#kirenai kara nasi                        
                        f=0
                        break
                    tempans+=1
                    shiro=[0]*len(shiro)
                    j-=1
                    break   
            if f==0:
                tempans=H*W
                break
            j+=1
            #print(j,shiro,"tochu") 
            
        #print(tempans,"tempans")
        ans=min(ans,tempans)
    print(ans)
#%%submit!
resolve()