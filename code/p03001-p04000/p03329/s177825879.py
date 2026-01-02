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
        self.INF = 5000000000000000

    def add_edge(self, from_v, to_v, cost):
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


if __name__ == '__main__':
    N = int(input())
    dij = Dijkstra(N + 1)
    for i in range(1, N + 1):
        dij.add_edge(i, i - 1, 1)
        j = 6
        while j <= i:
            dij.add_edge(i, i - j, 1)
            j *= 6
        j = 9
        while j <= i:
            dij.add_edge(i, i - j, 1)
            j *= 9
    dij.compute_shortest_distance(N)
    print(dij.distance[0])
