class Weigthed_Graph:
    #入力定義
    def __init__(self,vertex=[]):
        self.vertex=list(vertex)
        self.edge_number=0
        self.adjacent={v:{} for v in vertex}
    
    #頂点の追加
    def add_vertex(self,*adder):
        for u in adder:
            if u not in self.adjacent:
                self.adjacent[u]={}
                self.vertex.append(u)

    #辺の追加
    def add_edge(self,From,To,Weight):
        for w in [From,To]:
            if w not in self.adjacent:
                self.add_vertex(w)

        self.adjacent[From][To]=Weight
        
    #辺を除く
    def remove_edge(self,From,To):
        for w in [From,To]:
            if w not in self.adjacent:
                self.add_vertex(w)

        try:
            del self.adjacent[From][To]
        except:
            pass

    #頂点を除く
    def remove_vertex(self,*v):
        for u in v:
            for w in self.vertex:
                try:
                    del self.adjacent[w][u]
                except:
                    pass
            del self.adjacent[u]
    #Walkの追加

    #Cycleの追加
        
    #頂点の交換
            
    #グラフに頂点が存在するか否か
    def vertex_exist(self,v):
        try:
            _=self.adjacent[v]
            return True
        except:
            return False

    #グラフに辺が存在するか否か
    def edge_exist(self,From,To):
        try:
            _=self.adjacent[From][To]
            return True
        except:
            return False

    #出近傍
    def in_neighbohood(self,v):
        try:
            return list(self.adjacent[v].keys())
        except:
            return None

    #出次数
    def in_degree(self,v):
        try:
            return len(self.adjacent[v])
        except:
            pass
        

    #頂点数
    def vertex_count(self):
        return len(self.vertex)

    #辺数
    
    #頂点vを含む連結成分

    #距離

    #最短路

def Dijkstra(G,From,To):
    inf=float("inf")

    Q={v:inf for v in G.vertex}
    Q[From]=0
    
    while Q:
        u=min(Q,key=lambda x:Q[x])        
        if u==To:
            return Q[u]
        
        for v in G.adjacent[u]:
            if v in Q:
                Q[v]=min(Q[v],Q[u]+G.adjacent[u][v])

        del Q[u]
#-------------------------------------------------
X,Y=map(int,input().split())

A=sorted([X,Y,-X,-Y,0])
W=Weigthed_Graph(A)
for k in range(4):
    W.add_edge(A[k],A[k+1],A[k+1]-A[k])
W.add_edge(X,-X,1)
W.add_edge(-X,X,1)
W.add_edge(Y,-Y,1)
W.add_edge(-Y,Y,1)
print(Dijkstra(W,X,Y))
