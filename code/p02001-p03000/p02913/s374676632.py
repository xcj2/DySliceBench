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
    
#------------
from collections import defaultdict

N = int(input())
S =input()

rh = RollingHash(S)

#長さlenが上位園を満たすか二分探索
#条件を満たすためには，S[i:i+len]のhash値を計算．S[i:i+len]==S[j:j+len] and j-i>=lenならok
#ここで，i,jでループを回すのではなく，iで回してその時の{ハッシュ値:i}を辞書に持っておく．

#長さlが条件を満たすか？
def test(len):
    dd = defaultdict(int)
    for i in range(N-len+1):
        h=rh.hash(i,i+len)
        if dd[h]!=0:
            if i-dd[h]+1>=len:#+1の理由は下記のコメントを参照
                return True
        else:
            dd[h]=i+1#本当はiにしたいけど，i=0でやばい
    return False
        

ok=-1
ng=N
while abs(ng-ok)>1:
    med = (ng+ok)//2
    if test(med):
        ok=med
    else:
        ng=med

print(ok)