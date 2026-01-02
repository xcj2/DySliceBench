#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
import copy

def main():
    mod=10**9+7
    S=list(input())
    T=list(input())
    ns=len(S)
    nt=len(T)
    
    ans=[]#ここに候補を突っ込む，残りの?は全部aにしておく，最後にソートして一番小さいのを出力
    
    #Sのn文字目からTが始まるとして，行ける？
    def match(n):
        for i in range(nt):
            #文字不一致かつ?じゃないならダメ
            if S[n+i]!=T[i]:
                if S[n+i]!="?":
                    return False
                    
        return True
    
    #Sのn文字目からTに変更
    def make(n):
        temp=copy.deepcopy(S)
        for i in range(nt):
            temp[n+i]=T[i]
        for i in range(ns):
            if temp[i]=="?":
                temp[i]="a"
               
        a=(''.join(map(str, temp)))
        return a
    
    
    
    for i in range(ns-nt+1):
        if match(i):
            ans.append(make(i))
            
    if len(ans)!=0:      
        ans.sort()
        print(ans[0])
    else:
        print("UNRESTORABLE")
        

    

main()
