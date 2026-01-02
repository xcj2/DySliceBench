import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():

    ##########################################
    import heapq
    class Dijkstra():
        """
        ・有向 / 無向は問わない(無向の場合は，逆向きの辺もたす)
        ・負のコストがない場合のみ
        ・計算量はO(E log|V|)　
        ・heapを使うことで頂点を走査する必要がなくなる（代わりに，距離更新したものは確定でなくともqueに入れておく）
        ・復元なし
        """

        #最短のpathをたす


        class Edge():
            #重み付き有向辺

            def __init__(self, _to, _cost):
                self.to =_to
                self.cost = _cost

        def __init__(self, V):
            #引数Vは頂点数
            self.inf=10**20
            self.G = [[] for _ in range(V)] #隣接リストG[u][i]が頂点uのi番目の辺
            self. _E = 0 #辺の数
            self._V = V #頂点数

        #proparty - 辺の数
        def E(self):
            return self._E

        #proparty - 頂点数
        def V(self):
            return self._V

        def add(self, _from, _to, _cost):
            #2頂点と辺のコストを追加
            self.G[_from].append(self.Edge(_to,_cost))
            self._E +=1

        def add2(self, _from, _to, _cost):
            #2頂点と辺のコスト（無向）を追加
            self.G[_from].append(self.Edge(_to, _cost))
            self.G[_to].append(self.Edge(_from, _cost))
            self._E +=2

        def shortest_path(self,s):#,g):
            #始点sから頂点iまでの最短経路長のリストを返す
            que = [] #priority queue
            d = [self.inf] * self.V()

            #prev = [None]*self.V() #prev[j]は，sからjへ最短経路で行くときのjの一つ前の場所
            #復元で使う

            d[s] = 0
            heapq.heappush(que,(0,s)) #始点の距離と頂点番号をヒープに追加

            while len(que)!=0:
                #キューに格納されてある中で一番コストが小さい頂点を取り出す
                cost,v = heapq.heappop(que)

                #キューに格納された最短経路長候補がdの距離よりも大きい場合に処理をスキップ
                if d[v] < cost:
                    continue

                #頂点vに隣接する各頂点iに対して，vを経由した場合の距離を計算して，これがd[i]よりも小さい場合に更新
                for i in range(len(self.G[v])):
                    e = self.G[v][i] #vのi個目の隣接辺
                    if d[e.to] > d[v] + e.cost:
                        d[e.to] = d[v] + e.cost #更新

                        #prev[e.to] = v
                        #復元で使う

                        heapq.heappush(que,(d[e.to],e.to)) #queに新たな最短経路長候補を追加

            """#sからgまでの最短経路
            path = []
            pos = g #今いる場所，ゴールで初期化
            for _ in range(self.V()+1):
                path.append(pos)
                if pos == s:
                    break
                #print("pos:",format(pos))
                pos = prev[pos]
            path.reverse()
            #print(path)"""

            return d#,path
    ########################
    ################
    class UnionFind():
        """
        parents : 親要素(findしない場合は根ではないことの注意)，根の場合は"-(要素数）"
        find(x):要素xの属するグループの根を返す
        size(x):要素xの属するグループの要素数を返す
        same(x,y):x,yが同じグループに属しているか返す
        重いかも！　　members(x):要素xが属するグループに属する要素をリストで返す
        roots():全ての根の要素を返す
        group_count():グループの数を返す
        重いかも！　all_group_members():{根要素：[そのグループに含まれる要素のリスト]}の辞書を返す
        """
        def __init__(self, n):
            self.n = n
            self.parents = [-1] * n

        def find(self, x):
            #根を探す&つなぎかえる
            if self.parents[x] < 0:
                return x
            else:
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)

            if x == y:
                return

            if self.parents[x] > self.parents[y]:
                x, y = y, x

            self.parents[x] += self.parents[y]
            self.parents[y] = x

        def size(self, x):
            return -self.parents[self.find(x)]

        def same(self, x, y):
            return self.find(x) == self.find(y)

        def members(self, x):
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]

        def roots(self):
            return [i for i, x in enumerate(self.parents) if x < 0]

        def group_count(self):
            return len(self.roots())

        def all_group_members(self):
            return {r: self.members(r) for r in self.roots()}

        def __str__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    ################


    mod=10**9+7
    H,W=MI()
    ch,cw=MI()
    dh,dw=MI()
    ch+=1
    cw+=1
    dh+=1
    dw+=1
    
    S=[]
    S.append(["#"]*(W+4))
    S.append(["#"]*(W+4))
    for i in range(H):
        s=["#"]*2 + list(input()) + ["#"]*2
        S.append(s)
    S.append(["#"]*(W+4))
    S.append(["#"]*(W+4))
    
    
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    
    dx2=[-2,-2,-2,-2,-2,  -1,-1,-1,-1,   0,0,   1, 1,1,1,   2, 2,2,2,2]
    dy2=[-2,-1, 0, 1, 2,  -2,-1, 1, 2,  -2,2,  -2,-1,1,2,  -2,-1,0,1,2]
    
    uf=UnionFind((W+4)*(H+4))
    
    for i in range(H+2):
        for j in range(W+2):
            if S[i][j]==".":
                for k in range(4):
                    ii=i+dx[k]
                    jj=j+dy[k]
                    if S[ii][jj]==".":
                        fro=i*(W+4)+j
                        to=ii*(W+4)+jj
                        uf.union(fro,to)
    
    roots=[[-1]*(W+4) for _ in range(H+4)]
    for i in range(H+4):
        for j in range(W+4):
            if S[i][j]==".":
                now=i*(W+4)+j
                root=uf.find(now)
                roots[i][j]=root
                
    roots_uf=uf.roots()
    from collections import defaultdict
    dd = defaultdict(int)
    
    cur=0
    for v in roots_uf:
        dd[v]=cur
        cur+=1
    
    djk=Dijkstra(len(roots_uf))
                
                
    for i in range(2,H+2):
        for j in range(2,W+2):
            if S[i][j]==".":
                for k in range(20):
                    ii=i+dx2[k]
                    jj=j+dy2[k]
                    if S[ii][jj]==".":
                        fro=roots[i][j]
                        to=roots[ii][jj]
                        if fro!=to:
                            djk.add(dd[fro],dd[to],1)
                            
    
    s=dd[roots[ch][cw]]
    g=dd[roots[dh][dw]]
    D=djk.shortest_path(s)
    ans=D[g]
    if ans>=10**6+5:
        ans=-1
    print(ans)                
    
    
                

main()
