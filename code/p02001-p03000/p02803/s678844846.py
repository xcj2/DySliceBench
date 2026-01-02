class Graph:
    #入力定義
    def __init__(self,vertex=[]):
        self.vertex=list(vertex)
        self.edge_number=0
        self.adjacent={v:set() for v in vertex}

    #頂点の追加
    def add_vertex(self,*adder):
        k=len(self.vertex)
        m=0

        for u in adder:
            if u not in self.adjacent:
                self.adjacent[u]=set()
                self.vertex.append(u)

    #辺の追加
    def add_edge(self,From,To):
        for w in [From,To]:
            if w not in self.adjacent:
                self.add_vertex(w)

        if To not in self.adjacent[From]:
            self.adjacent[From].add(To)
            self.adjacent[To].add(From)
            self.edge_number+=1

    #辺を除く
    def remove_edge(self,u,v):
        for w in [u,v]:
            if w not in self.adjacent:
                self.add_vertex(w)

        if u in self.adjacent[v]:
            self.adjacent[u].remove(v)
            self.adjacent[v].remove(u)
            self.edge_number-=1

    #頂点を除く
    def remove_vertex(self,*v):
        for w in v:
            if w in self.adjacent:
                self.edge_number-=len(self.adjacent[w])
                for u in self.adjacent[w]:
                    self.adjacent[u].remove(w)
                del self.adjacent[w]


    #Walkの追加
    def add_walk(self,*walk):
        n=len(walk)
        for i in range(n-1):
            self.add_edge(walk[i],walk[i+1])

    #Cycleの追加
    def add_cycle(self,*cycle):
        self.add_walk(*cycle)
        self.add_edge(cycle[-1],cycle[0])

    #頂点の交換
    def __vertex_swap(self,p,q):
        self.vertex.sort()

    #グラフに頂点が存在するか否か
    def vertex_exist(self,v):
        return v in self.adjacent

    #グラフに辺が存在するか否か
    def edge_exist(self,u,v):
        if not(self.vertex_exist(u) and self.vertex_exist(v)):
            return False
        return u in self.adjacent[v]

    #近傍
    def neighbohood(self,v):
        if not self.vertex_exist(v):
            return []
        return list(self.adjacent[v])

    #次数
    def degree(self,v):
        if not self.vertex_exist(v):
            return 0

        return len(self.adjacent[v])

    #頂点数
    def vertex_count(self):
        return len(self.vertex)

    #辺数
    def edge_count(self):
        return self.edge_number

    #頂点vを含む連結成分
    def connected_component(self,v):
        if v not in self.adjacent:
            return []

        from collections import deque
        T={u:False for u in self.adjacent}
        T[v]=True
        S=deque([v])

        while S:
            u=S.popleft()
            for w in self.adjacent[u]:
                if not T[w]:
                    T[w]=True
                    S.append(w)

        return [x for x in self.adjacent if T[x]]

    #距離
    def distance(self,u,v):
        from collections import deque
        inf=float("inf")
        T={v:inf  for v in self.adjacent}

        if u==v:
            return 0

        Q=deque([u])
        T[u]=0
        while Q:
            w=Q.popleft()
            for x in self.adjacent[w]:
                if T[x]==inf:
                    T[x]=T[w]+1
                    Q.append(x)
                    if x==v:
                        return T[x]
        return inf

    #ある1点からの距離
    def distance_all(self,u):
        from collections import deque
        inf=float("inf")
        T={v:inf  for v in self.adjacent}

        Q=deque([u])
        T[u]=0
        while Q:
            w=Q.popleft()
            for x in self.adjacent[w]:
                if T[x]==inf:
                    T[x]=T[w]+1
                    Q.append(x)
        return T

    #最短路
    def shortest_path(self,u,v):
        from collections import deque
        inf=float("inf")
        T={v:[] for v in self.vertex}

        if u==v:
            return 0

        Q=deque([u])
        T[u]=[u]
        while Q:
            w=Q.popleft()
            for x in self.adjacent[w]:
                if not T[x]:
                    T[x]=T[w]+[x]
                    Q.append(x)
                    if x==v:
                        return T[x]
        return None

    #グラフの直径
    def diameter(self):
        from collections import deque
        inf=float("inf")

        u=self.vertex[0]
        T={u:inf  for u in self.vertex}

        Q=deque([u])
        T[u]=0
        while Q:
            w=Q.popleft()
            for x in self.adjacent[w]:
                if T[x]==inf:
                    T[x]=T[w]+1
                    Q.append(x)

        w=max(T,key=lambda x:T[x])
        T={u:inf  for u in self.vertex}

        Q=deque([w])
        T[w]=0
        while Q:
            w=Q.popleft()
            for x in self.adjacent[w]:
                if T[x]==inf:
                    T[x]=T[w]+1
                    Q.append(x)
        w=max(T,key=lambda x:T[x])
        return T[w]

def Grid_Graph(m,n):
    E=[]
    for x in range(1,m+1):
        E+=[(x,y) for y in range(1,n+1)]

    G=Graph(E)
    H=[(1,0),(0,1)]

    for y in range(1,n+1):
        for x in range(1,m+1):
            for a,b in H:
                p=x+a
                q=y+b
                if 1<=p<=m and 1<=q<=n:
                    G.add_edge((x,y),(p,q))
    return G
#====================================================
H,W=map(int,input().split())

G=Grid_Graph(W,H)
for y in range(H):
    S=input()
    for x in range(W):
        if S[x]=="#":
            G.remove_vertex((x+1,y+1))

M=-1
for a in G.adjacent:
    U=G.distance_all(a)
    M=max(M,max(U.values()))
print(M)