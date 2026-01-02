import heapq
import math
class Graph:
    def __init__(self,v,adj,w_v = None):
        super().__init__()
        self.v = v
        self.w_e = [{} for _ in [0]*self.v]
        self.neighbor = [[] for _ in [0]*self.v]
        
        self.w_v = w_v

        for i, adj_i in enumerate(adj):
            for j, w in enumerate(adj_i):
                self.w_e[i][j] = w #weight of edge
                self.neighbor[i].append(j)

    def dijkstra(self,v_n):
        d = [10**18]*self.v
        d[v_n] = 0
        prev = [-1]*self.v

        queue = []
        for i,d_i in enumerate(d): heapq.heappush(queue,(d_i,i))
        
        while len(queue)>0:
            d_u,u = queue.pop()
            if d[u]<d_u :continue
            for v in self.neighbor[u]:
                alt = d[u]+self.w_e[u][v]
                if d[v]>alt:
                    d[v] = alt
                    prev[v] = u
                    heapq.heappush(queue,(alt,v))

        return d,prev
    
    def WarshallFloyd(self):
        d = [[10**18]*self.v for _ in [0]*self.v]
        for i in range(self.v):
            for j in self.neighbor[i]:
                d[i][j] = self.w_e[i][j]
                
        for i in range(self.v):
            for j in range(self.v):
                for k in range(self.v):
                    check = d[i][k] + d[k][j]
                    if d[i][j] > check:
                        d[i][j] = check
        return d

def main():
    n = int(input())

    a = [[int(t)for t in input().split()]for _ in [0]*n]

    g = Graph(n,a)
    a_check = g.WarshallFloyd()

    s = 0
    for i in range(n):
        for j in range(n):
            a_ij = a[i][j]
            if a_ij != a_check[i][j]:
                print(-1)
                return
            if sum([a_ij == a[i][k] + a[k][j] for k in range(n) if k != i and k != j]) == 0:
                s+=a_ij
    print(s//2)

if __name__ == "__main__":
    main()
