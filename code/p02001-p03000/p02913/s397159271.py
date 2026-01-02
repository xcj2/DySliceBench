
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    class RollingHash(object):
        """
        construct: O(N)
        query:
            hash: O(1)
            lcp: O(logN)
            search: O(N)
        """
        __base1=1007; __mod1=10**9
        __base2=1009; __mod2=10**7

        def __init__(self,s):
            """
            s: str
            """
            n=len(s)
            self.__s=s
            self.__n=n
            b1=self.__base1; m1=self.__mod1
            b2=self.__base2; m2=self.__mod2
            H1,H2=[0]*(n+1),[0]*(n+1)
            P1,P2=[1]*(n+1),[1]*(n+1)
            for i in range(n):
                H1[i+1]=(H1[i]*b1+ord(s[i]))%m1
                H2[i+1]=(H2[i]*b2+ord(s[i]))%m2
                P1[i+1]=P1[i]*b1%m1
                P2[i+1]=P2[i]*b2%m2
            self.__H1=H1; self.__H2=H2
            self.__P1=P1; self.__P2=P2

        @property
        def str(self):
            return self.__s

        @property
        def len(self):
            return self.__n

        def hash(self,l,r=None):
            """
            l,r: int (0<=l<=r<=n)
            return (hash1,hash2) of S[l:r]
            """
            m1=self.__mod1; m2=self.__mod2
            if r is None: r=self.__n
            assert 0<=l<=r<=self.__n
            return ((self.__H1[r]-self.__P1[r-l]*self.__H1[l]%m1)%m1,
                    (self.__H2[r]-self.__P2[r-l]*self.__H2[l]%m2)%m2)

        @classmethod
        def lcp(cls,rh1,rh2,l1,l2,r1=None,r2=None):
            """
            rh1,rh2: RollingHash object
            l1,l2,r1,r2: int 0<=l1<=r1<=r1.len,0<=l2<=r2<=rh2.len
            return lcp length between rh1[l1:r1] and rh2[l2:r2]
            """
            if r1 is None: r1=rh1.__n
            if r2 is None: r2=rh2.__n
            assert 0<=l1<=r1<=rh1.__n and 0<=l2<=r2<=rh2.__n
            L=0
            R=min(r1-l1,r2-l2)
            if rh1.hash(l1,l1+R)==rh2.hash(l2,l2+R): return R
            while(R-L>1):
                H=(L+R)//2
                if rh1.hash(l1,l1+H)==rh2.hash(l2,l2+H): L=H
                else: R=H
            return L

        @classmethod
        def search(cls,pattern,text):
            """
            pattern,text: RollingHash object
            return list of index i's satisfying text[i:] starts with pattern
            """
            n=text.__n; m=pattern.__n
            res=[]
            for i in range(n-m+1):
                if text.hash(i,i+m)==pattern.hash(0,m):
                    res.append(i)
            return res
    
    mod=10**9+7
    N=I()
    S=input()
    rh=RollingHash(S)
    
    from collections import defaultdict

    """
    長さlのpunがあるか
    S[i:i+l]のハッシュ値と，S[j:j+l]のハッシュ値が同じかつ，i+l <= jなら良い．
    i,jのループで回さず，iだけ回してハッシュ値とその時のiを記憶しておく．同じハッシュ値が出てきたらi+l < jの判定をする
    """
    def ch(l):
        dd = defaultdict(lambda: -1)# ハッシュ => i
        for i in range(N-l+1):
            h=rh.hash(i,i+l)
            if dd[h]!=-1:
                ii=dd[h]
                if ii+l <= i:
                    return True
            else:
                dd[h]=i
                
        return False
        
        
    
    ok=0
    ng=N
    while ng-ok>1:
        med=(ok+ng)//2
        if ch(med):
            ok=med
        else:
            ng=med
            
    print(ok)
    
    
    
    

    

main()
