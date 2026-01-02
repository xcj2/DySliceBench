#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    X,=pin()


    #解が存在することが証明されているので、探索を行う
    for a in range(1000):
        cond=0        
        if a**5==X:print(a,0);break
        #search B for B**5==t
        A=a
        if A**5<X:#Bは負！
            t=X-A**5
            cond=1#後で負にする
            r=A+1 #rはBのかりの最大値
        elif A**5>X:
            t=(A**5)-X
            r=100+A+1
        #search B for B**5==t
        #print(a,t,cond,"K")
        for b in range(r):                
            #print(b**5,t)
            if b**5==t:
                #print("yeah")
                B=b
                if cond==1:B*=(-1)
                print(A,B)
                return
                
#%%submit!
resolve()