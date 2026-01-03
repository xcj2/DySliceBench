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
    dL=[[0,0] for _ in range(N)]
    
    q=queue.Queue()
    
    #0,N-1からの距離
    for j in range(2):
        if j==0:
            q.put((0,0,0))#v,pare,d
        else:
            q.put((N-1,N-1,0))#v,pare,d
        while not q.empty():
            v,p,d=q.get()
            dL[v][j]=d
            for i in range(len(adj[v])):
                nv=adj[v][i]
                if nv!=p:
                    q.put((nv,v,d+1))
                    
    s=0
    for i in range(N):
        if dL[i][0]>dL[i][1]:
            s+=1
    
        
    
    if s>=N-s:
        print("Snuke")
    else:
        print("Fennec")
     
        
    
    

main()
