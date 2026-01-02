import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
class EulerTour(object):
    def __init__(self,E,root=0):
        """
        E: list of int (adjacency list)
        root: int
        """
        n=len(E)
        self.__V=list(range(n))
        self.__E=E
        self.__begin=[0]*n
        self.__end=[0]*n
        self.__tour=[0]*(2*n-1)
        self.__k=0
        self.__dfs(root,-1)
        del self.__k

    def __dfs(self,v,p):
        self.__begin[v]=self.__k
        self.__tour[self.__k]=v
        self.__k+=1
        for u in self.__E[v]:
            if u==p: continue
            self.__dfs(u,v)
            self.__tour[self.__k]=v
            self.__k+=1
        self.__end[v]=self.__k

    @property
    def begin(self):
        return self.__begin

    @property
    def end(self):
        return self.__end

    @property
    def tour(self):
        return self.__tour

def resolve():
    # input
    n,q=map(int,input().split())
    E=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=map(lambda x:int(x)-1,input().split())
        E[a].append(b)
        E[b].append(a)
    # build
    tree=EulerTour(E)
    # calculate
    imos=[0]*(2*n)
    for _ in range(q):
        p,x=map(int,input().split())
        p-=1
        imos[tree.begin[p]]+=x
        imos[tree.end[p]]-=x
    for i in range(2*n-1):
        imos[i+1]+=imos[i]
    # output
    print(*[imos[tree.begin[i]] for i in range(n)])
resolve()