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
def dp_resolvea():
    #シミュレーションをないーーーぶにやると(|s|^2+1)//2回必要なのでTLEするよ（乱択でごまかす方法をおもいつきませんでした）
    #一番長い移動を考えると、全部Rだった場合の
    #状態を圧縮するとシミュレーションできませんか？
    S=input()
    N=len(S)
    ans=[[1]*N,[0]*N]
    
    for i in range(1<<20):#2^20回くりかえしたら10^5回より増えるやろ->当然の権利のようにTLEします
        ans[(i+1)%2]=[0]*N
        for n in range(1,N-1):
            if S[n]=="R":ans[(i+1)%2][n]+=ans[i%2][n-1]
            else:ans[(i+1)%2][n]+=ans[i%2][n+1]
    
    print(*ans[0])
    return            

def dp_resolve():
    #そうです、状態遷移の回数を圧縮します　    
    S=input()
    N=len(S)
    dp=[[0]*N for i in range(20)]
    
    #ダブリングをするために、貰うDPにしたい
    #dp[moves][initial_position]=initial_positionの人のmoves回後のます(操作を数列の変換としてあつかう、とも言います）
    henkan=[0]*N
    for n in range(N):
        if S[n]=="R":
            henkan[n]=n+1
        else:henkan[n]=n-1
    #print(henkan)
    dp[0]=henkan
    
    for i in range(1,20):#25回だ！
        for m in range(N):
            dp[i][m]=dp[i-1][dp[i-1][m]]
    #print(dp)
    ans=[0]*N
    for k in range(N):
        ans[dp[-1][k]]+=1
    print(*ans)
    #これを20回にしたい
    #print(*ans[0])
    return              
def search_resolve():
    S=input()
    
    #Sのうち、連続する2文字が”RL”か、文末にだけ1以上がある
    #RLの効果が及ぶところごとに分割しよっか　LRの真ん中で分割
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
    
def resolve():
    dp_resolve()
    #search_resolve()
#%%submit!
resolve()