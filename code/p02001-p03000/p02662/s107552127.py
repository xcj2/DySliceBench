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
    #つまり、集合A,Sに対して、[x^s]PI(1+x^a_i) (f_i)

    #次に、Aの部分集合について考える
    #サンプル1の場合、N==3なので8個の部分集合がある
    #つまり、F3＝1+(f_1+f_2+f_3)+(f1_f2+f2_f3+f3_f1)+f1_f2_f3を考える
    #果たして、一般的なNにたいして多項式時間でにFnをもとめれば指数時間は完全回避できる
    #F3=(1+f1+f2+f1f2)+f3{(1+f1+f2+f1f2)}
    #  =(1+f3)(1+f1+f2+f1f2)
    #  =(f3で追加された新しいところ)(N=2のときのすべての部分集合)

    #これは、f3をSの部分集合にふくめるか、含めないかの探索と同等
    #一般的にFn=F_n-1*(1+fn)=PI(1+fn)とわかる

    #求めるものは[x^S]PI(1+fn)=[x^S]PI(2+x^a)

    from collections import defaultdict #本当は良くないがわかりやすさのためココに置く
    from copy import deepcopy
    
    ans=defaultdict(int)#i
    ans[0]=1 #init ,1=x^0より
    #print(ans)
    for a in A:
        #ans そのものと、ansの係数にx^aをかけたものを足し算    
        temp=defaultdict(int)
        for x in ans:
            if x+a<=S:
                temp[x+a]=ans[x]
            
            ans[x]*=2
            ans[x]%=mod
        for t in temp:
            if t<=S:
                ans[t]+=temp[t]
                ans[t]%=mod
    print(ans[S])    
    
#%%submit!
resolve()
        
    