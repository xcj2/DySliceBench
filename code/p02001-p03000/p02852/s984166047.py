import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

class SegmentTree(object):
    def __init__(self,A,dot,e):
        n=2**((len(A)-1).bit_length())
        self.__n=n
        self.__dot=dot
        self.__e=e
        self.__node=[e]*(2*n)
        for i in range(len(A)):
            self.__node[i+n]=A[i]
        for i in range(n-1,-0,-1):
            self.__node[i]=dot(self.__node[2*i],self.__node[2*i+1])

    def update(self,i,c):
        i+=self.__n
        node=self.__node
        node[i]=c
        while(i!=1):
            i//=2
            node[i]=self.__dot(node[2*i],node[2*i+1])

    def sum(self,l,r):
        vl,vr=self.__e,self.__e
        l+=self.__n; r+=self.__n
        while(l<r):
            if(l%2==1):
                vl=self.__dot(vl,self.__node[l])
                l+=1
            l//=2
            if(r%2==1):
                r-=1
                vr=self.__dot(self.__node[r],vr)
            r//=2
        return self.__dot(vl,vr)

def resolve():
    n,m=map(int,input().split())
    S=list(map(lambda x:int(x),input()))
    dp=[INF]*(n+1)
    dp[-1]=0
    tree=SegmentTree(dp,min,INF)
    for i in range(n-1,-1,-1):
        if(S[i]): continue
        s=tree.sum(i,min(i+m+1,n+1))
        dp[i]=s+1
        tree.update(i,s+1)

    if(dp[0]==INF):
        print(-1)
        return

    now=0
    val=dp[0]
    path=[]
    for i,x in enumerate(dp):
        if(x==INF): continue
        if(x<val):
            path.append(i-now)
            now=i
            val=x

    print(*path)
resolve()