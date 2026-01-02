import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def bisect(l,r,f,discrete=True,left=True):
    """
    l,r: l<r int if discrete else float
    f: function defined on [l,...,r] to {False,True}
    if discrete: f defined on Z; else: R
    if left: f satisfies that there uniquely exists d such that iff i<=d then f(i)
    else: iff i>=d then f(i) is True
    return d such as those above
    """
    assert r>l
    if discrete: assert isinstance(l,int) and isinstance(r,int)
    eps=1 if discrete else 10**-12
    if (not left)^f(r): return r if left else r+1
    elif left^f(l): return l-1 if left else l
    while(r-l>eps):
        h=(l+r)//2 if discrete else (l+r)/2
        if (not left)^f(h): l=h
        else: r=h
    return h if not discrete else l if left else r
    
class RollingHash(object):
    """
    construct: O(N)
    query:
        hash: O(1)
        lcp: O(logN)
    """
    __base1=1007; __mod1=10**9
    __base2=1009; __mod2=10**7

    def __init__(self,S):
        """
        S: str
        """
        n=len(S)
        self.__n=n
        b1=self.__base1; m1=self.__mod1
        b2=self.__base2; m2=self.__mod2
        H1,H2=[0]*(n+1),[0]*(n+1)
        P1,P2=[1]*(n+1),[1]*(n+1)
        for i,s in enumerate(S):
            H1[i+1]=(H1[i]*b1+ord(s))%m1
            H2[i+1]=(H2[i]*b2+ord(s))%m2
            P1[i+1]=P1[i]*b1%m1
            P2[i+1]=P2[i]*b2%m2
        self.__H1=H1; self.__H2=H2
        self.__P1=P1; self.__P2=P2

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

def resolve():
    n=int(input())
    S=input()
    # d=0ではtrue,d=nではfalseなので、そこでbisectする
    rh=RollingHash(S)
    def judge(d):
        # initialize
        J={rh.hash(i,i+d):-1 for i in range(n-d+1)}
        for i in range(n-d+1):
            h=rh.hash(i,i+d)
            if J[h]!=-1:
                if i-J[h]>=d: return True
            else: J[h]=i
        return False
    print(bisect(0,n,judge))
resolve()