import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
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

    mod=998244353
    N=I()
    X=[0]*N
    D=[0]*N
    
    for i in range(N):
        X[i],D[i]=MI()
    
    X,D=zip(*sorted(zip(X,D)))
    
    dp=[0]*(N+1)
    """
    dp[i]はi番目まで見たときと通り数，後ろから見てく．
    i番目を動かさないならば，dp[i+1]
    i番目を動かすならば，連鎖していき，影響が出ないところまで見る
    この連鎖分をセグ木で事前計算しておく．
    """
    seg=SegTree(N,0,max)
    seg.setL(range(N))
    # セグ木は，何番目まで影響するか，を持つ
    
    import bisect 
    
    for i in range(N-1,-1,-1):
        t=X[i]+D[i]
        num=bisect.bisect_left(X,t)
        l=i
        r=num
        M=seg.query(l,r)
        seg.update(i,M)
        
    dp[-1]=1
    for i in range(N-1,-1,-1):
        temp=seg.query(i,i+1)
        dp[i]=(dp[i+1]+dp[temp+1])%mod
        
    print(dp[0])
    
    # for i in range(N):
    #     print(dp[i])
        

main()
