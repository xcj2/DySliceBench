class Digraph:
    #入力定義
    def __init__(self,vertex=[]):
        self.vertex=set(vertex)

        self.edge_number=0
        self.vertex_number=len(vertex)

        self.adjacent_out={v:{} for v in vertex} #出近傍(vが始点)
        self.adjacent_in={v:{} for v in vertex} #入近傍(vが終点)

    #頂点の追加
    def add_vertex(self,*adder):
        for v in adder:
            if v not in self.vertex:
                self.adjacent_in[v]={}
                self.adjacent_out[v]={}

                self.vertex_number+=1
                self.vertex.add(v)

    #辺の追加(更新)
    def add_edge(self,From,To,weight=1):
        for v in [From,To]:
            if v not in self.vertex:
                self.add_vertex(v)

        if To not in self.adjacent_in[From]:
            self.edge_number+=1

        self.adjacent_out[From][To]=weight
        self.adjacent_in[To][From]=weight

    #辺を除く
    def remove_edge(self,From,To):
        for v in [From,To]:
            if v not in self.vertex:
                self.add_vertex(v)

        if To in self.adjacent_out[From]:
            del self.adjacent_out[From][To]
            del self.adjacent_in[To][From]
            self.edge_number-=1

    #頂点を除く
    def remove_vertex(self,*vertexes):
        for  v in vertexes:
            if v in self.vertex:
                self.vertex_number-=1

                for u in self.adjacent_out[v]:
                    del self.adjacent_in[u][v]
                    self.edge_number-=1
                del self.adjacent_out[v]

                for u in self.adjacent_in[v]:
                    del self.adjacent_out[u][v]
                    self.edge_number-=1
                del self.adjacent_in[v]

    #Walkの追加
    def add_walk(self,*walk):
        pass

    #Cycleの追加
    def add_cycle(self,*cycle):
        pass

    #頂点の交換
    def __vertex_swap(self,p,q):
        self.vertex.sort()

    #グラフに頂点が存在するか否か
    def vertex_exist(self,v):
        return v in self.vertex

    #グラフに辺が存在するか否か
    def edge_exist(self,From,To):
        if not(self.vertex_exist(From) and self.vertex_exist(To)):
            return False
        return To in self.adjacent_out[From]

    #近傍
    def neighbohood(self,v):
        if not self.vertex_exist(v):
            return []
        return list(self.adjacent[v])

    #出次数
    def out_degree(self,v):
        if not self.vertex_exist(v):
            return 0

        return len(self.adjacent_out[v])

    #入次数
    def in_degree(self,v):
        if not self.vertex_exist(v):
            return 0

        return len(self.adjacent_in[v])

    #次数
    def degree(self,v):
        if not self.vertex_exist(v):
            return 0

        return self.out_degree(v)-self.in_degree(v)

    #頂点数
    def vertex_count(self):
        return len(self.vertex)

    #辺数
    def edge_count(self):
        return self.edge_number

    #頂点vを含む連結成分
    def connected_component(self,v):
        pass

#Warshall–Floyd
def Warshall_Floyd(D):
    """Warshall–Floyd法を用いて,全点間距離を求める.

    D:負Cycleを含まない有向グラフ
    """
    T={v:{} for v in D.vertex} #T[u][v]:uからvへ
    for u in D.vertex:
        for v in D.vertex:
            if v==u:
                T[u][v]=0
            elif v in D.adjacent_out[u]:
                T[u][v]=D.adjacent_out[u][v]
            else:
                T[u][v]=float("inf")

    for u in D.vertex:
        for v in D.vertex:
            for w in D.vertex:
                T[v][w]=min(T[v][w],T[v][u]+T[u][w])

    return T
#================================================
from itertools import permutations
N,M,R=map(int,input().split())
Y=list(map(int,input().split()))
D=Digraph(list(range(1,N+1)))
for _ in range(M):
    a,b,c=map(int,input().split())
    D.add_edge(a,b,c)
    D.add_edge(b,a,c)

Dist=Warshall_Floyd(D)

Z=float("inf")
for P in permutations(Y):
    X=0
    for i in range(R-1):
        X+=Dist[P[i]][P[i+1]]
    Z=min(Z,X)
print(Z)