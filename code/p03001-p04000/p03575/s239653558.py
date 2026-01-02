#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
sys.setrecursionlimit(10**9)
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
#グラフの閉路検出だけ
def resolve():
    N,M=pin()
    gragh={(v+1):[] for v in range(N)}
    for i in range(M):
        a,b=pin()
        gragh[a].append(b)
        gragh[b].append(a)
    #print(gragh)#->ok
    heiro=dict()
    heiro2=set()
    def dfs(v_from,travel,prev=None):
        tra=list(travel)    
        for v_to in gragh[v_from]:
            #stoper
            if v_to==prev:
                #print("a")
                continue
            if v_to in(tra):#closed 
                dicset=set()
                f=0
                kyori=0
                for n,t in enumerate(tra):
                    if v_to==t:
                        f=1
                    if f==1:
                        kyori+=1
                        dicset.add(t)
                if len(dicset)>2:
                    dicset=frozenset(dicset)
                    heiro.setdefault(dicset,kyori)
                    #print(gragh[v_from],(prev,v_from,v_to),dicset,tra)
                    break
                continue
            #caller
            prev=v_from
            tra2=tra[:]
            tra2.append(v_to)  
            #print(tra,v_to) 
            dfs(v_to,tra2,prev)

        return
        
    dfs(1,[1])
    #print(heiro)
    for j in (heiro.keys()):
        temp=set(j)
        #print(temp)
        for k in temp:
            heiro2.add(k)
    #print(heiro2)
    seen=heiro2.copy()
    global ans
    def dfs2(f):
        global ans
        if  f in seen:return
        ans+=1
        seen.add(f)
        for t in gragh[f]:
            dfs2(t)
            
    ans=0        
    for i in range(1,N+1):
        if i in seen:continue
        dfs2(i)
    if len(heiro2)==0:ans-=1
    print(ans)    
#%%submit!
resolve()