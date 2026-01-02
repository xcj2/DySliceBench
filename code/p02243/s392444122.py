import queue


class Edge:
    def __init__(self, from_v, to_v, cost):
        self.from_v = from_v
        self.to_v = to_v
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def get_from_v(self):
        return self.from_v

    def get_to_v(self):
        return self.to_v

    def get_cost(self):
        return self.cost


class Vertex:
    def __init__(self, cost, id):
        self.cost = cost
        self.id = id

    def __lt__(self, other):
        return self.cost < other.cost

    def get_cost(self):
        return self.cost

    def get_id(self):
        return self.id


class Dijkstra:
    def __init__(self, number_of_vertex):
        # self.edges = []
        self.graf = [[] for _ in range(number_of_vertex)]
        self.number_of_vertex = number_of_vertex
        self.distance = []  # 最短距離
        self.INF = 1145141919810

    def add_edge(self, from_v, to_v, cost):
        # self.edges.append(Edge(from_v, to_v, cost))
        self.graf[from_v].append(Edge(from_v, to_v, cost))

    def compute_shortest_distance(self, start):
        self.distance = [self.INF] * self.number_of_vertex
        self.distance[start] = 0
        que = queue.PriorityQueue()

        que.put(Vertex(0, start))

        while not que.empty():
            top = que.get()
            cost = top.get_cost()
            id = top.get_id()
            if self.distance[id] < cost: continue
            for a_edge in self.graf[id]:
                to_v = a_edge.get_to_v()
                from_v = a_edge.get_from_v()
                prev_cost = self.distance[from_v]
                next_cost = self.distance[to_v]
                if next_cost > prev_cost + a_edge.get_cost():
                    next_cost = prev_cost + a_edge.get_cost()
                    self.distance[to_v] = next_cost
                    que.put(Vertex(next_cost, to_v))


n = int(input())
dij = Dijkstra(n)

for i in range(n):
    tmp = list(map(int, input().split()))
    u = tmp[0]
    k = tmp[1]
    vc = tmp[2:]
    for j in range(k):
        dij.add_edge(u, vc[2 * j], vc[2 * j + 1])

dij.compute_shortest_distance(0)

for i in range(n):
    print(str(i) + " " + str(dij.distance[i]))

