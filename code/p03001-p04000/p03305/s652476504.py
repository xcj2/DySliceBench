import heapq

class SegmentTree(object):
    def __init__(self, A, dot, unit):
        n = 1 << (len(A) - 1).bit_length()
        tree = [unit] * (2 * n)
        for i, v in enumerate(A):
            tree[i + n] = v
        for i in range(n - 1, 0, -1):
            tree[i] = dot(tree[i << 1], tree[i << 1 | 1])
        self._n = n
        self._tree = tree
        self._dot = dot
        self._unit = unit

    def __getitem__(self, i):
        return self._tree[i + self._n]

    def update(self, i, v):
        i += self._n
        self._tree[i] = v
        while i != 1:
            i >>= 1
            self._tree[i] = self._dot(self._tree[i << 1], self._tree[i << 1 | 1])

    def add(self, i, v):
        self.update(i, self[i] + v)

    def sum(self, l, r):
        l += self._n
        r += self._n
        l_val = r_val = self._unit
        while l < r:
            if l & 1:
                l_val = self._dot(l_val, self._tree[l])
                l += 1
            if r & 1:
                r -= 1
                r_val = self._dot(self._tree[r], r_val)
            l >>= 1
            r >>= 1
        return self._dot(l_val, r_val)

INF = float("inf")
YEN = pow(10,15)
n,m,s,t = map(int,input().split())
s-=1;t-=1 #s,tを0index
yedge = [[] for _ in range(n)]
sedge = [[] for _ in range(n)]
for i in range(m):
  u,v,a,b = map(int,input().split())
  u-=1;v-=1
  yedge[u].append([a,v]);yedge[v].append([a,u])
  sedge[u].append([b,v]);sedge[v].append([b,u])

def dijkstra_heap(s,edge):
    #始点sから各頂点への最短距離
    d = [float("inf")] * n
    used = [True] * n #True:未確定。始点として探索されたか。というかdが更新されたか。
    d[s] = 0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist,e)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        #まだ使われてない頂点の中からスタートから最小の距離のものを探す
        if not used[minedge[1]]: #すでに探索済みの場合にはスキップして次のプライオリティーキューへ。
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = False #ここで始点として探索済みにする。
        for e in edge[v]:
            if used[e[1]]: #行き先がすでに始点として探索済みでない場合には値を更新。
                heapq.heappush(edgelist,[e[0]+d[v],e[1]]) #重みをスタートからの最短重みにするため+d[v]
    return d ##始点sから各頂点への最短距離がアウトプットとなる。  
yto = dijkstra_heap(s,yedge)
#sto = dijkstra_heap(s,sedge)
#yot = dijkstra_heap(t,yedge)
sot = dijkstra_heap(t,sedge)
#print(yto)
#print(sto)
#print(yot)
#print(sot)
A = []
for i in range(n):
  if i == s:
    temp = sot[i]
  elif i == t:
    temp = yto[i]
  else:
    temp = yto[i]+sot[i]
  A.append(temp)
#print(A)
Tree = SegmentTree(A,min, INF)
for i in range(n):
  temp = Tree.sum(i,n)
  ans = YEN - temp
  print(ans)