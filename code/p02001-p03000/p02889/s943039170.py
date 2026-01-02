import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))


"""
全点対探索 & Nが小さいのでワーシャルフロイド．クエリも多めだし
合計距離から補給の回数をうまく計算するのは難しい，
残燃料を持つのも厳しい．
距離バージョンではなくて補給回数バージョンで新しいグラフとか作りたい

新しいグラフは距離がL以下の全点に対してならコスト1の辺を結ぶ．
最初からLあるのでコスト-1

"""
def main():
    
    def warshall_floyd(d):
        #d[i][j]: iからjへの最短距離
        N=len(d)
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d[i][j] = min(d[i][j],d[i][k] + d[k][j])
        return d
    
    mod=10**9+7
    N,M,L=MI()
    inf = 10**12
    d=[[inf]*N for _ in range(N)]
    for i in range(M):
        a,b,c=MI()
        a-=1
        b-=1
        d[a][b]=c
        d[b][a]=c
        
    d=warshall_floyd(d)
    
    nd=[[inf]*N for _ in range(N)] # 距離がL以下ならコスト1で結ぶ
    
    for i in range(N):
        for j in range(N):
            if d[i][j]<=L:
                nd[i][j]=1
    
    nd =warshall_floyd(nd)
    
    Q=I()
    for _ in range(Q):
        s,t=MI()
        s-=1
        t-=1
        ans=nd[s][t]
        if ans >= inf:
            ans=0
        print(ans-1)
        
    
    
    
main()
