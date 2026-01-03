#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
import queue

def main():
    mod=10**9+7
    N=I()
    adj=[[] for _ in range(N)]
    for i in range(N-1):
        a,b=MI()
        a-=1
        b-=1
        adj[a].append(b)
        adj[b].append(a)
    bit=[-1]*N#未確認,F,S    
    bit[0]=0
    bit[-1]=1
    pL=[0]*N
    dS=0
    
    q=queue.Queue()
    q.put((0,0,0))#v.pare,depth
    
    #深さを調べる
    while not q.empty():
        v,p,d=q.get()
        pL[v]=p
        if v==N-1:
            dS=d
            break
        for i in range(len(adj[v])):
            nv=adj[v][i]
            if nv!=p:
                q.put((nv,v,d+1))
    
    #主要なところを塗る            
    v=N-1            
    for _ in range((dS-1)//2):
        v=pL[v]
        bit[v]=1
        
    q2=queue.Queue()
    q2.put((0,0))#v.pare
    while not q2.empty():
        v,p=q2.get()
        if bit[v]==-1:
            bit[v]=bit[p]

        for i in range(len(adj[v])):
            nv=adj[v][i]
            if nv!=p:
                q2.put((nv,v))
        
        
                    
    s=sum(bit)#sunukeが塗れる
    if s>=N-s:
        print("Snuke")
    else:
        print("Fennec")
     
        
    
    

main()
