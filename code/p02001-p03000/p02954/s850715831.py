#print#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code

#別に誰も10^100なんて数が必要とはいってないのだ
def resolve():
    S=input()
    #シミュレーション真面目にやると|s|^2回必要なのでTLEするよ（乱択でごまかす方法をおもいつきませんでした）
    #状態を圧縮するとシミュレーションできませんか？
    #Sのうち、連続する2文字が”RL”か、文末にだけ1以上がある
    #RLの効果が及ぶところごとに分割しよっかLRの真ん中で分割
    N=len(S)
    sub=[N]#kugiri
    sub2=[]#"RL"のLの位置
    for i in range(N-1):
        cont=()
        if S[i]=="L"and S[i+1]=="R":
            sub.append(i+1)
        if S[i]=="R"and S[i+1]=="L":
            sub2.append(i+1)
    sub.sort(reverse=True)
    #print(sub,sub2)

    ans=[0]*N
    temp=[0,0]
    ind=0
    for i in range(N):
        l=sub2[ind]
        temp[(l-i)%2]+=1
        if i+1 in sub:
            ans[l]+=temp[0]
            ans[l-1]+=temp[1]
            temp=[0,0]
            ind+=1
            sub.pop()
            
            
    
    print(*ans)
    
    
#%%submit!
resolve()
