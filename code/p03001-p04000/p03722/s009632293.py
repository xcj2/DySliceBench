N,M=map(int,input().split())
graph=[[] for i in range(N+1)]
for _ in range(M):
    a,b,weight=map(int,input().split())
    graph[a].append((b,-weight))
    
class Node():
    def __init__(self,name):
        self.name=name
        self.par=None
        self.d=float("inf")
        
    def relax(self,other,weight):
        if self.d>other.d+weight:
            self.d=other.d+weight
            self.par=other.name
    def relax_(self,other,weight):
         if self.d>other.d+weight:
            self.d=other.d+weight
            return True
         return False
def bellman_ford(graph,s_node):
    N=len(graph)-1
    d_list=[Node(i) for i in range(N+1)]
    #初期化
    d_list[s_node].d=0
    for _ in range(N-1):
        #N回同じループを繰り返す
        for node in range(1,N+1):
            for tuple_ in graph[node]:
                point,distance=tuple_
                d_list[point].relax(d_list[node],distance)
    negative=[False for i in range(N+1)]
    for _ in range(N-1):
        #N回同じループを繰り返す
        for node in range(1,N+1):
            for tuple_ in graph[node]:
                point,distance=tuple_
                if d_list[point].relax_(d_list[node],distance):
                    if negative[point]==False:
                        negative[point]=True
                    else:
                        for que in graph[point]:
                            negative[que[0]]=True
    if negative[N]:
        return False

    return d_list[N].d

K=bellman_ford(graph,1)
if K!=False:
    print(-K)
else:
    print("inf")
