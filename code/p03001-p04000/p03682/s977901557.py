import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
import heapq
class Prim():
    """
    ・無向辺
    ・負のコストがあっても大丈夫？
    ・計算量はO(E log|V|)　
    ・heapを使う
    """
    
    class Edge():
        #重み付き有向辺（あとで往復させる）
        
        def __init__(self, _to, _cost):
            self.to =_to
            self.cost = _cost
    
    def __init__(self, V):
        #引数Vは頂点数
        self.G = [[] for _ in range(V)] #隣接リストG[u][i]が，頂点uのi番目の辺
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
        self._E +=1
        
    def CostSum(self):
        #print(self.G[0][0].cost)
        
        used = [0]*self.V()
        que = [] #priority queue
        heapq.heappush(que,(0,0)) #始点の距離と頂点番号=0をヒープに追加
        ans =0 #辺の長さの和
        
        while len(que)!=0:
            #print("que:",format(que))
            #キューに格納されてある中で一番コストが小さい頂点を取り出す
            cost,v = heapq.heappop(que)
            
            #すでにX内にあれば(使用ずみならば)処理しない
            if used[v] ==1:
                continue
            used[v] = 1
            ans += cost
            
            #現在の全域木Xから，Xの外にある頂点e.toとの距離を見てqueに入れていく
            for i in range(len(self.G[v])):
                e = self.G[v][i] #vのi個目の隣接辺
                #print("e:",format(e.to))
                if used[e.to]==0:
                    heapq.heappush(que,(e.cost,e.to))
                    
        return ans   



def main():
    mod=10**9+7
    N=I()
    xyi=[[0,0,0] for _ in range(N)]
    for i in range(N):
        xyi[i][0],xyi[i][1]=MI()
        xyi[i][2]=i
    xyi.sort()
    prim = Prim(N)
    for i in range(N-1):
        prim.add2(xyi[i][2],xyi[i+1][2],abs(xyi[i][0]-xyi[i+1][0]))
        
    xyi.sort(key=lambda x: x[1])
    for i in range(N-1):
        prim.add2(xyi[i][2],xyi[i+1][2],abs(xyi[i][1]-xyi[i+1][1]))

        
    ans = prim.CostSum()
    
    print(ans)
    

main()
