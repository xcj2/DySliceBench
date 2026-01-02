import heapq

class Adjlist_weighted():

    def __init__(self, nodes, edges = None):
        self.nodes = nodes
        lis = [{} for i in range(nodes)]
        if edges is not None:
            for edge in edges:
                lis[edge[0]][edge[1]] = edge[2]
        self.edges = lis

    def add_edge(self, edge):
        self.edges[edge[0]][edge[1]] = edge[2]
        self.edges[edge[1]][edge[0]] = edge[2]
        return self

    def next_edges(self,x):
        return self.edges[x]

class Min_span_tree():

    def __init__(self, graph):
        min_span_tree = Adjlist_weighted(graph.nodes)
        searched_nodes = [False]*graph.nodes
        start = 0
        heap = [(0, start, start)]
        total_length = 0
        while heap:
            (cost, now, prev) = heapq.heappop(heap)
            if not searched_nodes[now]:
                searched_nodes[now] = True
                if (now, prev) != (start, start):
                    min_span_tree.add_edge((prev, now, cost))
                cand = graph.next_edges(now)
                total_length += cost
                for next in cand:
                    if not searched_nodes[next]:
                        heapq.heappush(heap, (cand[next], next, now))
        self.min_span_tree = min_span_tree
        self.total_length = total_length
    

(V, E) = tuple(map(int, input().split(" ")))
graph = Adjlist_weighted(V)
for _ in range(E):
    graph.add_edge(tuple(map(int, input().split(" "))))
mst = Min_span_tree(graph)
print(mst.total_length)
