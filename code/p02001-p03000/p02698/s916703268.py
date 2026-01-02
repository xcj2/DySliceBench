import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    import bisect
    
    N=I()
    A=LI()
    adj=[[]for _ in range(N)]
    
    for i in range(N-1):
        u,v=MI()
        u-=1
        v-=1
        adj[u].append(v)
        adj[v].append(u)
        
    #DFSで見ていく．オイラーツアーを作っておく．更新情報をstackに積んでおき，巻き戻る時にpopしていく
    
    #非再帰オイラーツアー
    #ETにオイラーツアー を，ET1,ET2はそれぞれ開始番号と終了番号．
    #stackで管理，行きがけと帰りがけをそれぞれi,~iで表現
    
    st_ch=[]
    #(どの場所を更新したか，元々の値は何か)を持っておく
    
    
    inf=10**10
    dp=[inf]*(N+1)
    #dp[i]は長さiを取れるときの最小末尾（普通のLISと同じ持ち方）
    dp[0]=0
    
    ans=[0]*N#答えを入れとく


    def EulerTour(n, X, i0=0):
        # 隣接グラフXを消費しながら，親リストPを作りながら進む．
        #i0が根
        P = [-1] * n
        st = [~i0, i0]
        ct = -1
        ET = []
        ET1 = [0] * n
        ET2 = [0] * n
        DE = [0] * n
        de = -1
        while st:
            #頂点 i を見る
            i = st.pop()
            
            #帰り際の処理，ここを入れる場合，オイラーツアーの最後に「-1」がつくので注意
            if i < 0:
                ct += 1
                # ↓ 戻りもETに入れる場合はこれを使う
                ET.append(P[~i])#notのnot
                ET2[~i] = ct
                de -= 1
                
                #dp-rollback
                num,val=st_ch.pop()
                dp[num]=val
                
                continue
            
            #行きがけの処理
            if i >= 0:
                ET.append(i)
                ct += 1
                if ET1[i] == 0: ET1[i] = ct
                de += 1
                DE[i] = de
                
                #dp-update
                num=bisect.bisect_left(dp,A[i])
                st_ch.append((num,dp[num]))#更新情報を入れておく
                dp[num]=A[i]#更新
                
                ans_num=bisect.bisect_left(dp,inf)
                ans[i]=ans_num-1
                
                #
                
                
            for a in X[i][::-1]:
                if a != P[i]:
                    P[a] = i
                    for k in range(len(X[a])):
                        if X[a][k] == i:
                            del X[a][k]
                            break
                    st.append(~a)
                    st.append(a)
        return (ET, ET1, ET2)
    
    EulerTour(N,adj)
    for i in range(N):
        print(ans[i])
    


                    
                
        
    

main()
