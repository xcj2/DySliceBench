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
        return self.__inv(self.sum(r-1),self.sum(l-1))

    def bisect_left(self,w,increase=True):
        n=self.__n
        k=2**((self.__n-1).bit_length())
        res=0
        now=self.__e
        while(k):
            if(res+k<=n and self.__dot(now,self.__node[res+k])<w and increase):
                now=self.__dot(now,self.__node[res+k])
                res+=k
            elif(res+k<=n and self.__dot(now,self.__node[res+k])>w and (not increase)):
                now=self.__dot(now,self.__node[res+k])
                res+=k
            k//=2
        return res

def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    idx=[0]*n
    for i,a in enumerate(A):
        idx[a-1]=i

    from operator import add
    bit=BIT([0]*n,add,0)

    ans=0
    for k in range(n,0,-1):
        i=idx[k-1]
        bit.add(i)
        s=bit.sum(i)
        l0=bit.bisect_left(s-1)-(s<=1)
        l1=bit.bisect_left(s-2)-(s<=2)
        r0=bit.bisect_left(s+1)
        r1=bit.bisect_left(s+2)
        ans+=k*((i-l0)*(r1-r0)+(l0-l1)*(r0-i))
    print(ans)
resolve()