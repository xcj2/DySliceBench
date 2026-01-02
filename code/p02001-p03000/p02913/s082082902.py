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
    get_hash: O(1)
    LCP: O(logN)
    """
    def __init__(self,S,m1=10**9+9,b1=1007,m2=10**9+7,b2=1009):
        """
        S: string
        m1>m2: prime sufficiently large
        b1,b2: base 0<bi<mi
        """
        assert m1>m2 and 0<b1<m1 and 0<b2<m2
        n=len(S)
        self.__n=n
        self.__m1=m1
        self.__m2=m2
        self.__H1,self.__H2=[0]*(n+1),[0]*(n+1)
        self.__P1,self.__P2=[1]*(n+1),[1]*(n+1)
        for i,s in enumerate(S):
            self.__H1[i+1]=(self.__H1[i]*b1+ord(s))%m1
            self.__H2[i+1]=(self.__H2[i]*b2+ord(s))%m2
            self.__P1[i+1]=self.__P1[i]*b1%m1
            self.__P2[i+1]=self.__P2[i]*b2%m2

    @property
    def len(self):
        return self.__n

    def hash(self,l,r=None):
        """
        l,r: int (0<=l<=r<=n)
        return (hash1,hash2) of S[l:r]
        """
        if r is None: r=self.len
        assert 0<=l<=r<=self.len
        return ((self.__H1[r]-self.__P1[r-l]*self.__H1[l]%self.__m1)%self.__m1,(self.__H2[r]-self.__P2[r-l]*self.__H2[l]%self.__m2)%self.__m2)

    def LCP(self,l1,r1=None,rh2=None,l2=0,r2=None):
        if r1 is None: r1=self.len
        if rh2 is None: rh2=self
        if r2 is None: r2=rh2.len
        assert 0<=l1<=r1<=self.len and 0<=l2<=r2<=rh2.len
        L=0
        R=min(r1-l1,r2-l2)
        if self.hash(l1,l1+R)==rh2.hash(l2,l2+R): return R
        while(R-L>1):
            H=(L+R)//2
            if self.hash(l1,l1+H)==rh2.hash(l2,l2+H): L=H
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