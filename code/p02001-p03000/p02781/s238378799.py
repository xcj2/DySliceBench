#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
def resolve():
    N=input()
    K,=pin()

    #degit DP
    #dp_table["index"][smaller][cond]=cond:=ちょうどK個の数がある を満たす総数
    
    rb=(0,1)
    dp_table=[[[0 for cnd in range(K+1)]for sml in rb]for ind in range(len(N)+1)]
    dp_table[0][0][0]=1
    #print(dp_table)
    #print("degit,sml,k,prove,l,x<n,dp_table[degit-1][sml][k]")#
    for degit in range(len(N)+1):
        n=int(N[degit-1])
        for sml in rb:
            t=10 if sml else int(N[degit-1])+1
            for k in range(K+1):
                for prove in range(t):
                    x=prove
                    try:#Indexerror
                        #print(degit,sml,k,prove,"l",x<n,dp_table[degit-1][sml][k])
                        #if  sml==False  and x==n:print(n,":") 
                        dp_table[degit][sml or x<n][k+(x!=0)]+=dp_table[degit-1][sml][k]
                    except :pass

    print(dp_table[-1][0][K]+dp_table[-1][1][K])
    #print(dp_table)
#%%submit!
resolve()
