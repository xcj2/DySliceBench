import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    N,M=MI()
    inf=10**16
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


    seg=SegTree(N+1,inf,min)
    
    L=[0]*M
    R=[0]*M
    C=[0]*M
    for i in range(M):
        l,r,c=MI()
        l-=1
        r-=1
        L[i]=l
        R[i]=r
        C[i]=c
        
    R,C,L=zip(*sorted(zip(R,C,L)))
        
    
    
    #rが小さいものから見て(rが同じならcが小さい)確定させていく
    now=0#確定させたとこと
    seg.update(0,0)
    
    for i in range(M):
        r=R[i]
        l=L[i]
        c=C[i]
        m=seg.query(l,now+1)#移動もとの範囲での最小値
        #seg.update(r,m+c)
        now=r
        
        #このままだと入力例3みたいに，コストは低いけどl,rがちかいみたいなのを先に処理してしまう
        #とりあえず右端だけ更新しとけばokか?
        
        if m+c<seg.query(now,now+1):
            seg.update(now,m+c)
        
        #print((l+1,r+1,c),now+1,m,m+c)
        """
        for ii in range(N):
            print(seg.query(ii,ii+1))"""
        
    ans=seg.query(N-1,N)

    
    
    if ans>=inf:
        print(-1)
    else:
        print(ans)
    
        
    
        
        
    

main()
