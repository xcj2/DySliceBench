import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

"""
ある頂点が白のとき，穴あき度の総和に与える影響を考える，
入力例2の1-2-3-4なら(0,3,3,0)この頂点2に注目，この3は，上下どちらもに黒があれば良い．上(2^1 - 1) * 下(2^2 - 1)=3．つまり全量 - all白

実際には子が多い．どこか2箇所の部分木に黒があれば良い=>余事象．
・全量：pow(2,N-1)，自分は白確定，墓はなんでも良い

・all白=1通り
・1個の部分木が黒*1通り（*1は残りall白の分）
「1この部分木が黒」はどう求める？　その部分木のサイズをnとして，2^n - 1．
その部分木のサイズはどう求める？　全方位木DPか=>端の頂点から詰めていけばいけそう

"""

def main():
    mod=10**9+7
    import queue
        
    N=I()
    adj=[[]for _ in range(N)]
    for i in range(N-1):
        x,y=MI()
        x-=1
        y-=1
        adj[x].append(y)
        adj[y].append(x)
        
    #2べきを持っておくか，
    POW=[1]
    for _ in range(N+5):
        temp=POW[-1]
        POW.append((temp*2)%mod)
        
    #各頂点のじすう
    deg=[0]*N
    for i in range(N):
        deg[i]=len(adj[i])
    
    
    L=[[]for _ in range(N)]#　各頂点からみて，個を根とする部分木のサイズを配列として持っておく    
    
    looked=[0]*N#qに突っ込むか
    used=[0]*N#計算を終えたか
    q=queue.Queue()
    
    for v in range(N):
        if len(adj[v])==1:
            q.put(v)
            L[v].append(0)
            looked[v]=1
            
    ans=[0]*N
    while not q.empty():
        v=q.get()
        
        S=sum(L[v])
        rem=(N-1)-S#まだ見ていない方向の合計，-1は自分自身
        temp=POW[N-1]#全体
        temp-=1#all白
        
        for s in L[v]:#1つの部分木にだけ黒があるパターンを引く
            temp-=POW[s]-1
            temp%=mod
            
        #1つの部分木にだけ黒があるパターンを引く，続き
        temp-=POW[rem]-1
        temp%=mod
            
        ans[v]=temp
        used[v]=1
        
        for nv in adj[v]:
            if used[nv]==0:
                L[nv].append(S+1)
            
            if looked[nv]==0:
                # nvの計算に必要な方向をしっかり見ていれば計算用のqに回す
                if len(L[nv])>=deg[nv]-1:
                    q.put(nv)
                    looked[nv]=1
                
                
    # print(ans)
    
    y=sum(ans)
    x=POW[N]
    
    res=(y*pow(x,mod-2,mod))%mod
    print(res)
    
        
    
        
    
    

main()