import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    """
    根を固定させたバージョンをまず考える．
    木dpをしたいのでノードに通り数を持たせる．
    通り数が同じでも部分木のサイズが異なると，親要素の通り数は変わる（1-2-3-4で2が親のときを想起）ので
    通り数と部分木のサイズは持つ必要あり．
    子要素が2つの時を考える，
    左がa通り+b個
    右がc通り+d個
    a+cを並び替えてa側でb通り，c側でd通りなので
    (a+c)Ca *b*d
    ということは，各子要素の通り数をai，サイズをbiとして，
    Πai * (Σbi)!/(Π(bi!))
    シグマの部分だけ後回し（調整）
    
    あとは全方位化
    """
    N=I()

    fact=[1,1]
    factinv=[1,1]
    inv=[0,1]
    
    for i in range(2, 2*N+10):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)
    
    adj=[[]for _ in range(N)]
    for i in range(N-1):
        a,b=MI()
        a-=1
        b-=1
        adj[a].append(b)
        adj[b].append(a)
        
    import queue
    
    P=[-1]*N#親リスト
    Q=queue.Queue()#BFSに使う
    R=[]#BFSでトポソしたものを入れる
    
    Q.put(0)#1回目では0を根とする
    
    #トポソ########################
    while not Q.empty():
        v=Q.get()
        R.append(v)
        for nv in adj[v]:
            if nv!=P[v]:
                P[nv]=v
                adj[nv].remove(v)#親につながる辺を消しておく
                Q.put(nv)
    
    #1が上りで，2が下り
    size1=[1]*N
    size2=[0]*N
    dp1=[1]*N
    dp2=[1]*N
    
    #先にサイズは求めておく
    for v in R[1:][::-1]:
        size1[P[v]]+=size1[v]
        
    for v in range(N):
        size2[v]=N-size1[v]
    
    for v in R[1:][::-1]:#根以外を後ろから
        dp1[v]=(dp1[v]*fact[size1[v]-1])%mod
        p=P[v]
        dp1[p]=(dp1[p]*dp1[v]*factinv[size1[v]])%mod
        
    #根だけ
    dp1[R[0]]=(dp1[R[0]]*fact[size1[R[0]]-1])%mod

        
    #累積和ではなく逆元で．ここではしっかり根から決まっていく
    for v in R[1:]:
        p=P[v]
        
        #下り部分，根側
        temp=dp2[p]
        
        # 親要素のdp1から自分のdp1を引くことで，親周りの自分以外の寄与を求めた
        temp2=(dp1[p]*pow(dp1[v],mod-2,mod))%mod
        temp=(temp*temp2)%mod
        
        
        temp=(temp*factinv[size1[p]-1]*fact[size1[v]])%mod#親のところは親要素の分を加味して1引く
        temp=(temp*factinv[size2[p]]*fact[size2[v]-1])%mod#逆側から見たときは，vがpの親に見える
        dp2[v]=temp
        
    for i in range(N):
        #上側と下側の塗り方を考慮して（これは結局，一番最初のa+bCaに近い）
        ans=(dp1[i]*dp2[i]*fact[N-1]*factinv[size1[i]-1]*factinv[size2[i]])%mod
        print(ans)
        
        
        
        
    
    
        
  
        

main()
