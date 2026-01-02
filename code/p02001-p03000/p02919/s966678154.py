import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
class BIT(object):
    def __init__(self,A,dot,e,inv=None):
        n=len(A)
        self.__n=n
        self.__dot=dot
        self.__e=e
        self.__inv=inv
        self.__node=['$']+A # 1-indexed
        for i in range(1,n+1):
            j=i+(i&-i)
            if(j<=n): self.__node[j]=dot(self.__node[i],self.__node[j])

    def add(self,i,w=1):
        i+=1
        while(i<=self.__n):
            self.__node[i]=self.__dot(self.__node[i],w)
            i+=i&-i

    def sum(self,i):
        i+=1
        res=self.__e
        while(i>0):
            res=self.__dot(res,self.__node[i])
            i-=i&-i
        return res

    def range_sum(self,l,r):
        assert(self.__inv)
        return self.__inv(self.sum(r),self.sum(l))

    def bisect_left(self,w,increase=True):
        if(w>self.sum(self.__n-1)): return self.__n
        n=2**((self.__n-1).bit_length())
        res=0
        while(n>0):
            if(res+n<=self.__n and ((w>self.__node[res+n])^(not increase))):
                w-=self.__node[res+n]
                res+=n
            n//=2
        return res

def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    idx=[0]*n
    for i,a in enumerate(A): idx[a-1]=i
    from operator import add
    bit=BIT([0]*n,add,0)

    # calculate
    ans=0
    for k in range(n,0,-1):
        i=idx[k-1]
        bit.add(i)
        s=bit.sum(i)
        l0=bit.bisect_left(s-1)-(s<=1)
        l1=bit.bisect_left(s-2)-(s<=2)
        r0=bit.bisect_left(s+1)
        r1=bit.bisect_left(s+2)
        ans+=k*((l0-l1)*(r0-i)+(r1-r0)*(i-l0))
    print(ans)
resolve()