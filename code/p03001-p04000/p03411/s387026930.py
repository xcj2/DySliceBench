class Weigthed_Digraph:
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

def Flow(D,source,sink):
    s,t=source,sink

    H={v:[] for v in D.vertex}

    for u in D.vertex:
        for v in D.adjacent_out[u]:
            F=[v,D.adjacent_out[u][v],None]
            F[2]=B=[u,0,F]
            H[u].append(F)
            H[v].append(B)

    def dfs(v,t,f):
        if v==t:
            return f

        U[v]=True
        for e in H[v]:
            w,cap,inv=e

            if cap and (not U[w]):
                d=dfs(w,t,min(f,cap))
                if d:
                    e[1]-=d
                    inv[1]+=d
                    return d
        return 0

    inf=float("inf")
    f=inf
    flow=0
    while f:
        U={v:False for v in D.vertex}
        f=dfs(s,t,inf)
        flow+=f
    return flow

#================================================
N=int(input())

R=[0]*N
for i in range(N):
    a,b=map(int,input().split())
    R[i]=(a,b)

B=[0]*N
for i in range(N):
    c,d=map(int,input().split())
    B[i]=(c,d)

D=Weigthed_Digraph([c*k for k in range(1,N+1) for c in [1,-1]])

for i in range(1,N+1):
    D.add_edge("s",i,1)
    D.add_edge(-i,"t",1)

for i in range(N):
    a,b=R[i]
    for j in range(N):
        c,d=B[j]

        if a<c and b<d:
            D.add_edge(i+1,-(j+1),1)

print(Flow(D,"s","t"))