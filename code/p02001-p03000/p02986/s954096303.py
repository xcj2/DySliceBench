import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

"""
他の色ならば長さ0として色毎にグラフを作りたいけど無理よな，持ち方的にも計算量的にも．

木なので道は1通り，LCAとかで最短距離求まる
max(d)=10**4なのは何かできそう？

u,vの経路上にx色のものが(何本あるか,距離合計がいくつか)が必要
(距離，[各色のcount])を持って計算すれば，uv間の距離，uv間に何回x色のものが出たか，は求まるが，x色の辺の距離合計がわからん

色の情報を距離に付与するのも厳しそう．

距離を変更して都度全部計算するのは無理なので，
最後の答えに差分を追加するか，差分更新するか

色を指定されたらその色の辺をO(1)で出せるようにしておいてから
スタート/ゴールの(u,v)を指定された時，「所望の辺を含むか?」を高速に求められれば良いか？
いや，同じ色にM個固まっていると，その色を見るときにM回で大変．例えば全部色1 & (u,v)が毎回変わるとして，Q回のなかで毎回O(N)個の辺を舐めることになる
一応，所望の辺を含むか，はLCAを考えれば行けそう?

u=>vの辺を構築しても，本数がO(N)とかになって結局舐める辺が多い
結局，あるルートに同じ色の辺が大量に固まっていると何もできん

あー，LCAなら(u,v)の距離ではなく，
根からuまで，根からvまで，根からlcaまで，
がそれぞれもとまればできるので，各頂点iに対して，その頂点までの(x色の本数，x色の合計)を持てば良い．
全ての頂点のこれは持てないのでクエリ先読みし，必要なものだけ．これならメモリはO(Q)．

だけど必要な色がN種類あったら距離求めるのN回やるのか？
いや，ある辺を見たとき，更新する色は1色のみだけなのでなんかできる．
色毎に[本数,合計]を持っておき，辺をなめていく
所望のu,v,lcaの頂点がきたときに該当色の[本数，合計]を記憶していく．

"""
def main():
    mod=10**9+7
    N,Q=MI()
    adj=[[]for _ in range(N)]
    from collections import defaultdict
    uv2cd = defaultdict(set)#各辺の色と長さがわかるように
    for _ in range(N-1):
        a,b,c,d=MI()
        a-=1
        b-=1
        c-=1
        adj[a].append(b)
        adj[b].append(a)
        uv2cd[(a,b)]=(c,d)
        uv2cd[(b,a)]=(c,d)
        
    # N: 頂点数
    # G[v]: 頂点vの子頂点 (親頂点は含まない)

    def EulerTour(n, X, i0):
        # 隣接グラフXを消費しながら，親リストPを作りながら進む．
        # i0が根
        
        P = [-1] * n#親
        st = [~i0, i0]
        ct = -1
        ET = []#オイラーツアー 
        ET1 = [0] * n#最初に出てくるとき
        ET2 = [0] * n#最後に出てくるとき
        DE = [0] * n#深さ
        de = -1
        while st:
            #頂点 i を見る
            
            i = st.pop()
            
            #帰り際の処理，ここを入れる場合，オイラーツアーの最後に「-1」がつくので注意
            if i < 0:
                #"""
                #↓ 戻りも数字を足す場合はこれを使う
                ct += 1
                # ↓ 戻りもETに入れる場合はこれを使う
                ET.append(P[~i])#notのnot
                #"""
                ET2[~i] = ct
                de -= 1
                continue
            
            #行きがけの処理
            if i >= 0:
                ET.append(i)
                ct += 1
                if ET1[i] == 0: ET1[i] = ct
                de += 1
                DE[i] = de
                
            for a in X[i][::-1]:
                if a != P[i]:
                    P[a] = i
                    for k in range(len(X[a])):
                        if X[a][k] == i:
                            del X[a][k]
                            break
                    st.append(~a)
                    st.append(a)
        return (ET, ET1, ET2, DE, P)

    # Euler Tour の構築
    S,F,Frev,depth,P=EulerTour(N,adj,0)
    """
    S:訪問順
    F:最初に出てくるとき(頂点の開始番号)
    Frev：最後に出てくるとき(頂点の終了番号)
    """

    # 存在しない範囲は深さが他よりも大きくなるようにする
    INF = (N, None)

    # LCAを計算するクエリの前計算
    M = 2*N
    M0 = 2**(M-1).bit_length()
    data = [INF]*(2*M0)
    for i, v in enumerate(S):
        data[M0-1+i] = (depth[v], i)
    for i in range(M0-2, -1, -1):
        data[i] = min(data[2*i+1], data[2*i+2])

    # LCAの計算 (generatorで最小値を求める)
    def _query(a, b):
        yield INF
        a += M0; b += M0
        while a < b:
            if b & 1:
                b -= 1
                yield data[b-1]
            if a & 1:
                yield data[a-1]
                a += 1
            a >>= 1; b >>= 1

    # LCAの計算 (外から呼び出す関数)
    def query(u, v):
        fu = F[u]; fv = F[v]
        if fu > fv:
            fu, fv = fv, fu
        return S[min(_query(fu, fv+1))[1]]
    
    QL=[]
    v2x = defaultdict(set)#ある頂点と紐づくクエリ．頂点vに来るときに，どの色を計算すべきか格納
    
    for _ in range(Q):
        x,y,u,v=MI()
        x-=1
        u-=1
        v-=1
        lca=query(u,v)
        QL.append((x,y,u,v,lca))
        v2x[(u)].add(x)
        v2x[(v)].add(x)
        v2x[(lca)].add(x)
    
    count_xv = defaultdict(int)#頂点と色を指定された時の出現回数
    dist_xv = defaultdict(int)#頂点と色を指定された時の距離合計
    
    #今見ているやつ
    count=[0]*N#色毎の出現回数
    dist=[0]*N#色毎の累積距離
    used=[0]*N#巡回済か
    used[0]=1
    
    dist_nonchange=[0]*N#色を無視した距離（頂点毎)
    dsum=0
    
    now=0
    for nxt in S[1:-1]:
        x,d=uv2cd[(now,nxt)]
        if used[nxt]==0:#行き
            count[x]+=1
            dist[x]+=d
            used[nxt]=1
            
            dsum+=d
            dist_nonchange[nxt]=dsum
            
            for xx in v2x[nxt]:#各頂点毎に，見なければならない色を見る
                count_xv[(xx,nxt)]=count[xx]
                dist_xv[(xx,nxt)]=dist[xx]
        else:#帰り
            count[x]-=1
            dist[x]-=d

            dsum-=d
        
        # print(now,nxt,x,d,dsum)    
        
        now=nxt
            

    for i in range(Q):
        x,y,u,v,lca=QL[i]
        # 全部の色の合計距離から，その頂点までの該当色分を全部引いて，新たにy*本数を足す
        tempu=dist_nonchange[u] - dist_xv[(x,u)] + y*count_xv[(x,u)]
        tempv=dist_nonchange[v] - dist_xv[(x,v)] + y*count_xv[(x,v)]
        templca=dist_nonchange[lca] - dist_xv[(x,lca)] + y*count_xv[(x,lca)]
        
        ans=tempu + tempv - 2*templca
        
        print(ans)
        # print()
        # print(i,x,y,u,v,lca)
        # print(tempu,tempv,templca,ans)
        # print(dist_nonchange[v], dist_xv[(x,v)], count_xv[(x,v)])

        
        
        
            
    
    

main()
