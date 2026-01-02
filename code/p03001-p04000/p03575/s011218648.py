import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    class Lowlink(object):
        """
        construct: O(V+E)
        """
        def __init__(self,edges,root=0):
            """
            edges: list of list of int (adjacency list)
            root: int
            """
            # initialization
            self.__n=len(edges)
            self.__edges=edges
            self.__count=0
            self.__ord=[-1]*self.__n
            self.__low=[-1]*self.__n
            self.__bridge=[]
            self.__articulation=[]
            # construct
            self.__dfs(root,-1)

        def __dfs(self,v,p): # p:parent
            self.__ord[v]=self.__count
            self.__low[v]=self.__count
            self.__count+=1
            isArticulation=False
            count=0 # DFS treeの子の数(rootのarticulate判定に必要)
            for u in self.__edges[v]:
                if self.__ord[u]==-1: # まだ見てない
                    count+=1
                    self.__dfs(u,v)
                    self.__low[v]=min(self.__low[v],self.__low[u])
                    if (self.__ord[v]<self.__low[u]): self.__bridge.append([min(u,v),max(u,v)])
                    if (p!=-1 and self.__ord[v]<=self.__low[u]): isArticulation=True
                elif u!=p: # uは見たけどvuは通ってない(=後退辺(backward edge))
                    self.__low[v]=min(self.__low[v],self.__low[u])
            if (p==-1 and count>=2): isArticulation=True
            if isArticulation: self.__articulation.append(v)

        @property
        def bridge(self):
            return self.__bridge

        @property
        def articulation(self):
            return self.__articulation

    # input
    n,m=map(int,input().split())
    edges=[[] for _ in range(n)]
    for _ in range(m):
        u,v=map(lambda x:int(x)-1,input().split())
        edges[u].append(v)
        edges[v].append(u)
    low=Lowlink(edges)
    print(len(low.bridge))

resolve()