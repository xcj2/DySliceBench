#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    #参考：https://qiita.com/Kiri8128/items/a011c90d25911bdb3ed3
    #というかマルパクリ...
    
    N,M=MI()
    adj=[[]for _ in range(N)]
    for i in range(N-1):
        x,y=MI()
        x-=1
        y-=1
        adj[x].append(y)
        adj[y].append(x)
        
    import queue
    
    P=[-1]*N#親リスト
    Q=queue.Queue()#BFSに使う
    R=[]#BFSでトポソしたものを入れる
    
    Q.put(0)#0を根とする
    
    #トポソ########################
    while not Q.empty():
        v=Q.get()
        R.append(v)
        for nv in adj[v]:
            if nv!=P[v]:
                P[nv]=v
                adj[nv].remove(v)#親につながるを消しておく
                Q.put(nv)
                
    #setting#############
    
    #merge関数の単位元
    unit=1
    #子頂点を根とした木の結果をマージのための関数
    merge=lambda a,b: (a*b)%M
    
    
    #マージ後の調整用(bottom-up時)，今回，木の中の要素が全部白というパターンがあるので+1
    adj_bu=lambda a,v:a+1
    #マージ後の調整用(top-down時)
    adj_td=lambda a,v,p:a+1
    #マージ後の調整用(最終結果を求める時)，今回，全部白はダメなので，aをそのまま返す
    adj_fin=lambda a,i:a
    
    #今回の問題では，調整においてvやpは不要だが，必要な時もあるため，残している．
    
    #Bottom-up#############
    #merge関数を使ってMEを更新し，adjで調整してdpを埋める
    #MEは親ノード以外の値を集約したようなもの
    
    ME=[unit]*N
    dp=[0]*N
    
    
    for v in R[1:][::-1]:#根以外を後ろから
        dp[v]=adj_bu(ME[v],v)#BU時の調整
        p=P[v]
        ME[p]=merge(ME[p],dp[v])#親に，子の情報を伝えている．ME[p]の初期値はunit
        #print(v,p,dp[v],ME[p])
        
    #最後だけ個別に考える
    dp[R[0]]=adj_fin(ME[R[0]],R[0])
    
    #print(ME)
    #print(dp)
    
    #Top-down##########
    #TDは最終的に，Top-down時のdpを入れるが，途中においては左右累積和の左から累積させたものを入れておく
    #メモリの省略のため
    
    TD=[unit]*N
    
    for v in R:
        #左からDP（結果をTDに入れておく）
        ac=TD[v]
        for nv in adj[v]:
            TD[nv]=ac
            ac=merge(ac,dp[nv])
            
        #右からDP(結果をacに入れて行きながら進めていく)
        ac=unit
        for nv in adj[v][::-1]:
            TD[nv]=adj_td(merge(TD[nv],ac),nv,v)##TDときの調整
            ac=merge(ac,dp[nv])
            dp[nv]=adj_fin(merge(ME[nv],TD[nv]),nv)#最終調整
        
        
    for i in range(N):
        print(dp[i])
        
    
    
        

main()
