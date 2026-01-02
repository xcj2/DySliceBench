import heapq
class Graph:
    def __init__(self,w_v,w_e):
        super().__init__()
        self.size = len(w_v)
        self.w_v = [v_i for v_i in w_v]#value of vartex
        self.w_e = [{} for _ in [0]*self.size]

        self.maxw = 0

        self.neighbor = [[] for _ in [0]*self.size]
        for a_i,b_i,w_i in w_e:
            self.w_e[a_i][b_i] = w_i#weight of edge
            self.w_e[b_i][a_i] = w_i#weight of edge

            self.neighbor[a_i].append(b_i)
            self.neighbor[b_i].append(a_i)
            self.maxw+=w_i

    def dijkstra(self,v_n):
        d = [self.maxw]*self.size
        d[v_n] = 0
        prev = [-1]*self.size

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
    n,x,y = tuple([int(t)for t in input().split()])

    w_v = [0]*n
    w_e = [(i,i+1,1) for i in range(n-1)]
    w_e.append((x-1,y-1,1))

    g = Graph(w_v,w_e)

    distance = [g.dijkstra(i)[0] for i in range(n)]

    res = [0]*n
    for dmin_ in distance:
        for d in dmin_:
            res[d] += 1

    for r in res[1:n]:
        print(r//2)

if __name__ == "__main__":
    main()