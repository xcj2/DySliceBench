import sys
import heapq


class Edge:
    def __init__(self, vertex_to, weight):
        self.vertex_to = vertex_to
        self.weight = weight


class Vertex:
    def __init__(self):
        self.distance = sys.maxsize
        self.fixed: bool = False
        self.edges_from_this_vertex = []


class DijkstraAlgorithm:
    def __init__(self, number_of_vertices):
        self._number_of_vertices = number_of_vertices
        self._number_of_edges = 0
        self._vertices = [Vertex() for _ in range(number_of_vertices)]
        self._priority_queue = []
        heapq.heapify(self._priority_queue)

    def add_vertex(self, from_index, to_index, weight):
        self._vertices[from_index].edges_from_this_vertex.append(Edge(to_index, weight))

    def calculate_shortest_paths(self, start_vertex_index):
        self._vertices[start_vertex_index].distance = 0
        heapq.heappush(self._priority_queue, (self._vertices[start_vertex_index].distance, start_vertex_index))
        while len(self._priority_queue) > 0:
            shortest_vertex_distance, shortest_vertex_index = heapq.heappop(self._priority_queue)
            self._vertices[shortest_vertex_index].fixed = True
            for c_edge in self._vertices[shortest_vertex_index].edges_from_this_vertex:
                if not self._vertices[c_edge.vertex_to].fixed:
                    distance_candidate = shortest_vertex_distance + c_edge.weight
                    if distance_candidate < self._vertices[c_edge.vertex_to].distance:
                        self._vertices[c_edge.vertex_to].distance = distance_candidate
                        heapq.heappush(self._priority_queue, (distance_candidate, c_edge.vertex_to))

    def print(self):
        for c_vertex in self._vertices:
            if c_vertex.distance == sys.maxsize:
                print('INF')
            else:
                print(c_vertex.distance)


def call_dijkstra_algorithm():
    inputs = list(map(int, input().strip().split(' ')))
    number_of_vertices = inputs[0]
    number_of_edges = inputs[1]
    start_vertex_index = inputs[2]
    dijkstra = DijkstraAlgorithm(number_of_vertices)

    for _ in range(number_of_edges):
        inputs = list(map(int, input().strip().split(" ")))
        from_index = inputs[0]
        to_index = inputs[1]
        weight = inputs[2]
        dijkstra.add_vertex(from_index, to_index, weight)

    dijkstra.calculate_shortest_paths(start_vertex_index)
    dijkstra.print()


if __name__ == '__main__':
    call_dijkstra_algorithm()

