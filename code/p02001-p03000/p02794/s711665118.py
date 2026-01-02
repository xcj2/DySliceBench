import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    """
    余事象：Q1~QMのどれかを満たさないものの数を数える
    「Q1を満たさない」は数えやすい．ここから包除
    """
    N=I()
    adj=[[]for _ in range(N)]
    from collections import defaultdict
    dd = defaultdict(int)
    
    for i in range(N-1):
        a,b=MI()
        a-=1
        b-=1
        
        #a<bにしておく
        if a>b:
            a,b=b,a
        adj[a].append(b)
        adj[b].append(a)
        dd[(a,b)]=1<<i#辺のid
        
    #popcount####################
    def popcount(x):
        '''xの立っているビット数をカウントする関数
        (xは64bit整数)'''

        # 2bitごとの組に分け、立っているビット数を2bitで表現する
        x = x - ((x >> 1) & 0x5555555555555555)

        # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
        x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

        x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
        x = x + (x >> 8) # 16bitごと
        x = x + (x >> 16) # 32bitごと
        x = x + (x >> 32) # 64bitごと = 全部の合計
        return x & 0x0000007f
    
    
    #LCA-経路復元########################
    # N: 頂点数
    # G[v]: 頂点vの子頂点 (親頂点は含まない)


    def EulerTour(n, X, i0):
        # 隣接グラフXを消費しながら，親リストPを作りながら進む．
        # i0が根
        
        P = [-1] * n
        st = [~i0, i0]
        ct = -1
        ET = []
        ET1 = [0] * n#最初に出てくるとき
        ET2 = [0] * n#最後に出てくるとき
        DE = [0] * n
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
    
    def make_route(u,v):
        #使う辺の集合を50bit整数で返す，u,vからそれぞれlcaまで
        
        e=0
        lca=query(u,v)
        for i in range(2):
            if i==1:
                v=u
            while v!=lca:
                p=P[v]
                if p<v:
                    e+=dd[(p,v)]
                else:
                    e+=dd[(v,p)]
                v=p
            
        return e
    #########################

    M=I()
    U=[0]*M
    V=[0]*M
    
    E=[]
    
    for i in range(M):
        U[i],V[i]=MI()
        U[i]-=1
        V[i]-=1
        E.append(make_route(U[i],V[i]))
        #print(i,bin(E[i]))
    
    ans=0
    for i in range(pow(2,M)):#使う条件の集合
        e=0#白にすべきところ
        for j in range(M):#j個目の制約に注目
            if (i>>j)&1:
                e2=E[j]
                e=e|e2#白く塗るべきところが増えていく
                
        temp=pow(2,(N-1)-popcount(e))#bitが0のところは各2通りなので
        #print(bin(i),bin(e),temp)
        if popcount(i)%2==0:#包除原理，立っているbitが偶数個ならプラス
            ans+=temp
        else:
            ans-=temp
            
    print(ans)
            
                
                
            
        
    

main()
