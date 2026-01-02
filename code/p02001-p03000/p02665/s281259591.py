import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    ####################
    import sys
    class Lazysegtree():
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
            #データの変更
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
            while L < R:
                if R & 1:
                    R -= 1
                    s = self.segf(s, self.data[R])
                if L & 1:
                    s = self.segf(s, self.data[L])
                    L += 1
                L >>= 1
                R >>= 1
            return s
        
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

            
    ##########
    
    mod=10**9+7
    N=I()
    A=LI()
    A[-1]-=1
    if A[0]!=0:
        ans=-1
            
    else:
        ans=N+1
        now=0#キャパがある最上位
        seg=Lazysegtree([1]*(N+1), 10**10, True, min)
        for i in range(1,N+1):
            a=A[i]
            if ans==-1:
                break
            while a>0:
                if now==i:
                    ans=-1
                    break
                
                cap=seg.query(now,now+1)
                #print("i:",i,",a:",a,",now:",now,",cap:",cap,",ans",ans)
                if a>=cap:
                    a-=cap
                    #seg.add(now,now+1,-cap)，now+=1するのでいらない
                    seg.add(now+1,i,cap)
                    ans+=(i-now)*cap
                    now+=1
                    #print(now,cap)
                else:
                    #print(now,cap,"--")
                    
                    seg.add(now,now+1,-a)
                    seg.add(now+1,i,a)
                    ans+=(i-now)*a
                    a=0
                    


                
            
            
    print(ans)
        

main()
