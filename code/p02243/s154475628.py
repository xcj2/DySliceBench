from heapq import heapify,heappop,heappush

class Graph:
    def __init__(self,V,E):
        self.V = V
        self.E = E

    def dijkstra(self,st):
        INF = 10**9+1
        D = [INF for i in range(len(self.V))]
        #D[i]:頂点iまでの距離
        D[st] = 0
        Q = [[0,st]]
        Used = set()
        #既に最短距離が確定した頂点の集合
        
        while len(Used) < len(self.V):
            p = heappop(Q)
            p_dist,p_ind = p[0],p[1]
            for e in self.E[p_ind]:
                to,cost = e[0],e[1]
                if to not in Used:
                    if D[to] > D[p_ind] + cost:
                        D[to] = D[p_ind] + cost
                        heappush(Q,[D[to],to])
            Used.add(p_ind)

        return D

def main():
    n = int(input())
    V = [i for i in range(n)]
    E = [set() for _ in range(n)]
    #E[i]:頂点iからの向かう先と重みの組
    #(to,cost) in E[i]は辺(i,to)の重みがcostであることを意味する
    for i in range(n):
        I = list(map(int,input().split()))
        for j in range(2,len(I)):
            if j % 2 == 0:
                E[i].add((I[j],I[j+1]))

    G = Graph(V,E)

    ans = G.dijkstra(0)
    for i in range(n):
        print(i,ans[i])

if __name__ == "__main__":
    main()

