import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    inf=10**6
    N,K=MI()
    P=LI()
    inf=10**6
    class SegTree:
        def __init__(self,N,ide,segfunc=min):
            self.ide_ele = ide
            """
            ex)
             最小値のセグ木 → +inf
              和のセグ木 → 0
              積のセグ木 → 1
              gcdのセグ木 → 0
            """
            
            self.segfunc=segfunc
            
            #num:N以上の最小の2のべき乗
            self.num =2**(N-1).bit_length()
            self.seg=[self.ide_ele]*2*self.num




        #リストで初期化する
        def setL(self,init_val):
            #init_valは操作する数列
            for i in range(N):
                self.seg[i+self.num-1]=init_val[i]    
            #built
            for i in range(self.num-2,-1,-1) :
                self.seg[i]=self.segfunc(self.seg[2*i+1],self.seg[2*i+2]) 


        #k番目の値をxに更新
        def update(self,k,x):
            k += self.num-1
            self.seg[k] = x
            while k:
                k = (k-1)//2
                self.seg[k] = self.segfunc(self.seg[k*2+1],self.seg[k*2+2])


        #[p,q)の区間に対するクエリへの応答
        def query(self,p,q):
            if q<=p:
                return self.ide_ele
            p += self.num-1
            q += self.num-2
            res=self.ide_ele
            while q-p>1:
                if p&1 == 0:
                    res = self.segfunc(res,self.seg[p])
                if q&1 == 1:
                    res = self.segfunc(res,self.seg[q])
                    q -= 1
                p = p//2
                q = (q-1)//2
            if p == q:
                res = self.segfunc(res,self.seg[p])
            else:
                res = self.segfunc(self.segfunc(res,self.seg[p]),self.seg[q])
            return res



    
    """
    長さKの尺取りぽく見るか．
    最小値が抜けて最大値が入る場合は不変．
    ただし，並び替え後も元の物と変わらない場合を何度かカウントしそう．
    事前に（元から昇順になっている長さKの列）の個数を数えておこうか．
    後からこれを引くのはダメ，事前に計算しておかないと，すでに照準になっているものを数えているのか数えていないのか不明になる．
    
    これは簡単に求まる．次が自分以上なら1をつけて，長さKの尺取りで和がKならおk．
    累積和の方が実装が楽かなあ
    """
    ans=1#最初のK個を並び替えたものは無条件で数える
    mseg=SegTree(N,inf,min)
    Mseg=SegTree(N,-1,max)
    mseg.setL(P)
    Mseg.setL(P)
    
    #累積和パート
    S=[0]*(N+1)
    for i in range(N-1):
        if P[i]<P[i+1]:
            S[i+1]=1
    #print(S)
            
    for i in range(N):
        S[i+1]+=S[i]
    
    m=min(P[:K])
    M=max(P[:K])
    cnt=0#最初と同じ配列のものを何回数えたか
    if S[K]==K:#最初のKこを並び替えたものを1回とすでに数えてしまっているのでチェック
        cnt+=1
        
    for i in range(K,N):
        if m==P[i-K] and P[i]>M:#最小値が抜けて，新しく入るのが最大値を更新するなら
            m=mseg.query(i-K+1,i+1)
            M=P[i]
        else:
            m=mseg.query(i-K+1,i+1)
            M=Mseg.query(i-K+1,i+1)
            #print(i,S[i]-S[i-K+1],S[i],S[i-K+1])
            if cnt==0:
                ans+=1
            elif S[i]-S[i-K+1]!=(K-1):
                ans+=1
            if S[i]-S[i-K+1]==(K-1):
                cnt+=1
                
        #print(i,m,M,ans,cnt)

            
    print(ans)
    #print(S)

main()
