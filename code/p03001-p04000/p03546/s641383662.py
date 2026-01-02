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
                self.add_vertex(w)

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

def Dijkstra_All(D,From,with_path=False):
    """Dijksta法を用いて,単一始点Fromからの距離を求める.

    D:辺の重みが全て非負の有向グラフ
    From:始点
    To:終点
    with_path:最短路も含めて出力するか?

    (出力の結果)
    with_path=True->(距離,最短経路の辿る際の前の頂点)
    with_path=False->距離
    """
    from copy import copy

    T={v:float("inf") for v in D.vertex}
    T[From]=0

    if with_path:
        Prev={v:None for v in D.vertex}

    Q=copy(D.vertex)

    Flag=False
    while Q:
        u=min(Q,key=lambda u:T[u])
        Q.remove(u)

        for v in D.adjacent_out[u]:
            if T[v]>T[u]+D.adjacent_out[u][v]:
                T[v]=T[u]+D.adjacent_out[u][v]

                if with_path:
                    Prev[v]=u

    if with_path:
        return (T,Prev)
    else:
        return  T

#逆グラフの作成
def Inverse_Graph(D):
    """有向グラフDの全ての辺の向きを変えたグラフを出力する.

    D:有向グラフ
    """
    from copy import deepcopy

    F=Digraph(D.vertex)

    F.edge_number=D.edge_number
    F.vertex_number=D.vertex_number

    F.adjacent_in=deepcopy(D.adjacent_out)
    F.adjacent_out=deepcopy(D.adjacent_in)

    return F

#================================================
H,W=map(int,input().split())

D=Digraph(range(10))
for i in range(10):
    C=list(map(int,input().split()))
    for j in range(10):
        D.add_edge(i,j,C[j])

D=Inverse_Graph(D)
T=Dijkstra_All(D,1)

Count={x:0 for x in range(-1,10)}

for _ in range(H):
    A=list(map(int,input().split()))
    for a in A:
        Count[a]+=1

X=0
for a in range(10):
    X+=Count[a]*T[a]

print(X)