from collections import defaultdict
import heapq


class Dijkstra:
    """
    dijkstraの最短経路問題を解く
    input:
        S: start node
        adj: adj[a]=[(b,dist)]//なんとなく
    """

    def __init__(self, start, num_node, adj):
        """
        adj: adj[a]=[(b,dist)]
        num_node: num of nodes
        dist: dist from start_node
        prev: 最短経路において、一つ前のノードを記憶。経路復元に使う?
        """
        self.start_node = start
        self.adj= adj
        self.num_node = num_node
        self.dist = [float('inf')]*num_node
        self.prev = defaultdict(lambda: None)

        # dist form S to S = 0
        self.dist[start] = 0

    def calc_dist(self):
        """
        最短経路 distを計算する
        Q: content (dist_from_start,node)
        Qはheapqとして使う。dist_from_startの小さい順になる
        Qには、dist*N+nodeを入れることで高速化
        """
        Q = []
        heapq.heappush(Q, self.start_node)
        while Q:
            dist_to_node, node = divmod(heapq.heappop(Q),self.num_node)
            # 現在の値よりも大きくて、更新にならない場合
            if self.dist[node] < dist_to_node:
                continue

            # 次のホップを計算する
            for nex,weight in self.adj[node]:
                cand = dist_to_node + weight

                if self.dist[nex] > cand:  # update
                    self.dist[nex] = cand
                    self.prev[nex] = node
                    heapq.heappush(Q, cand*self.num_node+nex)

    def get_dist(self, d):
        """
            startからdまでの距離を返す
            これの前にcalc()を実行しておく
            たどり着けない場合は、float('inf')がかえる
        """
        return self.dist[d]
    def get_path(self,dst):
        """
        startからdstまでのpathをlistでreturn
        valifyしてないので怪しい
        """
        cur=dst
        ret=[cur]
        while cur!=self.start_node:
            cur=self.prev[cur]
            ret.append(cur)
        return list(reversed(ret))
N,M,S = map(int,input().split())
edges=[list(map(int,input().split())) for _ in range(M)]
C=[list(map(int,input().split())) for _ in range(N)]

max_c=2501


def toId(node,cur):
    return node*max_c+cur

def revId(id):
    return id//max_c,id%max_c


states=N*max_c
adj=[[] for _ in range(states)]


for a,b,c,d in edges:
    a-=1
    b-=1
    for cc in range(max_c-c):
        adj[toId(a,cc+c)].append((toId(b,cc),d))
        adj[toId(b,cc+c)].append((toId(a,cc),d))

for i,(c,d) in enumerate(C):
    for cc in range(max_c-c):
        adj[toId(i,cc)].append(((toId(i,cc+c),d)))


#for i,a in enumerate(adj):
#    print("from {}".format(revId(i)))
#    for v,d in a:
#        print("\t: {} cost:{}".format(revId(v),d))
    
S=min(S,max_c-1)
start=toId(0,S)

D=Dijkstra(start,states,adj)
D.calc_dist()
for i in range(1,N):
    ans=float("inf")
    path=None
    for cc in range(max_c):
        if ans>D.get_dist(toId(i,cc)):
            ans=D.get_dist(toId(i,cc))
            path=D.get_path(toId(i,cc))
    print(ans)

