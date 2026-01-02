import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

"""
左から見る，モンスターが生きているならそいつが左端ギリギリになる位置に爆弾投下
区間減算，座圧
"""
def main():
    ####################
    import sys
    class Lazysegtree():
        #必ず単位元に注意すること！queryで1点の値のみを抽出するような場合でも，単位元とsegfuncがあってないとダメ！！


        """RAQ
        外から使うのは，query，add,updateくらいか

        """
        def __init__(self, A, intv, initialize = True, segf = min):
            """
            Aが初期配列，intvが単位元,segfが評価関数
            """

            #区間は 1-indexed で管理
            self.N = len(A)
            self.N0 = 2**(self.N-1).bit_length()
            self.intv = intv
            self.segf = segf
            self.lazy = [0]*(2*self.N0)
            if initialize:
                self.data = [intv]*self.N0 + A + [intv]*(self.N0 - self.N)
                for i in range(self.N0-1, 0, -1):
                    self.data[i] = self.segf(self.data[2*i], self.data[2*i+1]) 
            else:
                self.data = [intv]*(2*self.N0)

        def _ascend(self, k):
            k = k >> 1
            c = k.bit_length()
            for j in range(c):
                idx = k >> j
                self.data[idx] = self.segf(self.data[2*idx], self.data[2*idx+1]) \
                + self.lazy[idx]

        def _descend(self, k):
            k = k >> 1
            idx = 1
            c = k.bit_length()
            for j in range(1, c+1):
                idx = k >> (c - j)
                ax = self.lazy[idx]
                if not ax:
                    continue
                self.lazy[idx] = 0
                self.data[2*idx] += ax
                self.data[2*idx+1] += ax
                self.lazy[2*idx] += ax
                self.lazy[2*idx+1] += ax

        def update(self, k, x):
            #1点のデータの変更
            k = k + self.N0
            self.data[k] = x
            self._ascend(k)

        def query(self, l, r):
            #クエリ，[l,r)かな
            L = l+self.N0
            R = r+self.N0
            Li = L//(L & -L)
            Ri = R//(R & -R)
            self._descend(Li)
            self._descend(Ri - 1)

            s = self.intv 
            t = self.intv 
            while L < R:
                if R & 1:
                    R -= 1
                    t = self.segf(self.data[R],t)
                if L & 1:
                    s = self.segf(s, self.data[L])
                    L += 1
                L >>= 1
                R >>= 1
            return self.segf(s,t)

        def add(self, l, r, x):
            #区間加算，[l,r)かな
            L = l+self.N0
            R = r+self.N0

            Li = L//(L & -L)
            Ri = R//(R & -R)

            while L < R :
                if R & 1:
                    R -= 1
                    self.data[R] += x
                    self.lazy[R] += x
                if L & 1:
                    self.data[L] += x
                    self.lazy[L] += x
                    L += 1
                L >>= 1
                R >>= 1

            self._ascend(Li)
            self._ascend(Ri-1)

        #必ず単位元に注意すること！queryで1点の値のみを抽出するような場合でも，単位元とsegfuncがあってないとダメ！！


    ##########




    import bisect
    
    N,D,A=MI()
    X=[0]*N
    H=[0]*N
    for i in range(N):
        X[i],H[i]=MI()
    
    X,H=zip(*sorted(zip(X,H)))
    
    from collections import defaultdict
    dd = defaultdict(int)

    for i in range(N):
        dd[X[i]]=i
        
    ans=0
    inf=10**10
    seg=Lazysegtree(list(H),inf,segf=min)
    for i in range(N):
        h=seg.query(i,i+1)
        
        if h>0:
            cnt=(h+A-1)//A
            ans+=cnt
            l=i
            t=X[l]+2*D
            r=bisect.bisect_right(X,t)
            
            seg.add(l,r,-1*cnt*A)
            
    print(ans)
        
    
        
    

main()
