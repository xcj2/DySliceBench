#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
def resolve():
    N,S=pin()
    A=tupin()#調子にのるな
    mod=998244353

    #形式的冪級数を考える
    #普通の部分和ッ->集合内の各アイテムについて、選ぶか選ばないか。O(2^n)の探索
    #これを形式的冪級数でいえば、（1+x^a）を掛ける計算になる　指数時間ではない
    #つまり、集合A,Sに対して、[x^s]PI(1+x^a_i) (ひだりのカッコ部分をf_iとする)

    #次に、Aの部分集合、じゃなくて問題の区間について考える (ABC169と異なる部分はここ)
    #サンプル1の場合。区間に含まれるのは…って考える前に
    #区間なので終点があるね、a3が追加されることで終点にf3がある区間が追加されるよね
    #じゃあこれももしかしたら漸化式で作れるかも
    #F0=f0=1,F1=1+f1,F2=1+f1f2+f1+f2,F3=1+f1f2f3+f1f2+f1+f2f3+f2+f3...
    #F2=f2(f1+1)+f1+1 ,F3=f3(f1f2+f2+1)+f1f2+f1+f2+1=f3(f1f2+f2+1)+f2(f1+1)+f1+1
    #えっこれ漸化式の和？G3=f3(f1f2+f2+1)みたいに終点ごとにわける
    #G3=f3(f2(f1+1)+1)=f3(G2+1),G2=f2(f1+1)=f2(G1+1) Gn=fn(1+Gn-1)=(1+x^a)(1+Gn-1)
    #F3=G3+G2+G1=f2(G2+1)+G2+G1,
    #Fn+1-Fn=fn+1*(1+Gn)=(1+x^a_(n+1))*(1+Gn)=Gn+1=(1+x^a)(1+Gn)
    #FもGも漸化式で求められることがわかりました（？）

    from collections import defaultdict #本当は良くないがわかりやすさのためココに置く
    from copy import deepcopy

    F=defaultdict(int)
    G=defaultdict(int)
    F[0]=1 #init
    #F1-F0=f1*(1+G0)=f1+1
    #print(ans)
    for a in A:
        #G
        if len(G)==0:
            G[0]=1
            if a<=S:
                G[a]=1
        else:
            G[0]+=1
            temp=defaultdict(int)
            for g in G:
                temp[g]+=G[g]
                if g+a<=S:
                    temp[g+a]+=G[g]
                    temp[g+a]%=mod
            G=temp
            
        #Fの計算
        for g in G:
            F[g]+=G[g]
            F[g]%=mod
                    #print(F)
    print(F[S])



#%%submit!
resolve()
