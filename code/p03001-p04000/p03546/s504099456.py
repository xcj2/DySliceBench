import heapq
import math
class Graph:
    def __init__(self,v,w_e,w_v = None):
        super().__init__()
        self.v = v

        self.w_v = w_v
        self.w_e = [{} for _ in [0]*self.v]


        self.neighbor = [[] for _ in [0]*self.v]
        for a_i,b_i,w_i in w_e:
            self.w_e[a_i][b_i] = w_i#weight of edge
            self.neighbor[a_i].append(b_i)

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

def main():
    h,w = tuple([int(t)for t in input().split()])

    c = [[int(t) for t in input().split()]for _ in [0]*10]

    a = [[int(t) for t in input().split()]for _ in [0]*h]

    counter = [0]*10
    for a_i in a:
        for a_ij in a_i:
            if a_ij != -1:
                counter[a_ij]+=1

    w_e = []
    for i in range(10):
        for j in range(10):
            w_e.append((i,j,c[i][j]))
    
    g = Graph(10,w_e)

    routes = []
    for i in range(10):
        routes.append(g.dijkstra(i)[0])

    ans = 0
    for i in range(10):
        if i!=1:
            ans += routes[i][1]*counter[i]

    print(ans)


if __name__ == "__main__":
    main()